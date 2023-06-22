#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

double func(const vector <double> &x)
{
    return (x[0]-2)*(x[0]-2)+(x[1]-5)*(x[1]-5);
}
double func(const double &x1, const double &x2)
{
    return (x1-2)*(x1-2)+(x2-5)*(x2-5);
}
vector<double> newBazTochka(const vector <double> &x, const double &h)
{
    vector<double> z = x;
    double fz = func(z);

    if (func(z[0]+h, z[1]) < fz)
    {
        z[0] += h;
    } else if (func(z[0]-h, z[1]) < fz) { z[0] -= h; }
    fz = func(z);
    if (func(z[0], z[1]+h) < fz)
    {
        z[1] += h;
    } else if (func(z[0], z[1]-h) < fz) { z[1] -= h; }

    return z;
}

bool check(const double &e, const vector <double> &x, const vector <double> &z)
{
    return (fabs(x[0]-z[0]) < e && fabs(x[1]-z[1]) < e);
}

int main()
{
    // метод хука-дживса
    vector <double> x = {0, 2};
    double h = 0.1;
    double e = 0.0001;
    cout << "Значение в первой базисной точке: func(x) = func(" << x[0] << "; " << x[1] << ") = " << func(x) << endl;
    cout << "\tТекущая длина шага: " << h << endl;
    vector <double> z = x;
    int it = 0;
    while(h > e)
    {
        cout << "Итегация " << it << endl;
        cout << "\tЗначение в текущей базисной точке: func(z) = func(" << z[0] << "; " << z[1] << ") = " << func(z) << endl;
        z = newBazTochka(z, h);
        cout << "\tЗначение в новой базисной точке: func(z) = func(" << z[0] << "; " << z[1] << ") = " << func(z) << endl;
        cout << "\tТекущая длина шага: " << h << endl;
        if (!check(e, x, z))
        {
            while (true)
            {
                vector <double> P = {x[0] + 2*(z[0]-x[0]), x[1] + 2*(z[1]-x[1])};
                double fP = func(P);
                cout << "\tЗначение в точке образца: func(P) = func(" << P[0] << "; " << P[1] << ") = " << fP << endl;
                P = newBazTochka(P, h);
                fP = func(P);
                cout << "\tЗначение в новой точке образца: func(P) = func(" << P[0] << "; " << P[1] << ") = " << fP << endl;
                if (fP < func(z))
                {
                    x = z;
                    z = P;
                } else { x = z; break; }    
            }
        } else { h /= 10; }
        ++it;
    }
    cout << "Количество итераций: " << it << endl;
    cout << "\tf(x) = func(" << x[0] << "; " << x[1] << ") = " << func(x) << endl;
    cout << "\tf(z) = func(" << z[0] << "; " << z[1] << ") = " << func(z) << endl;

    return 0;
}
