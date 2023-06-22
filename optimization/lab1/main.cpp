#include <iostream>
#include <cmath>
#include <algorithm>
#include <tuple>
#include <vector>
#include <limits>

using namespace std;

double f(double x) { return (-4*x+exp(fabs(x-0.2))); }
double diff(double x, double _f(double x))
{
    const double h=1e-10;
    return (_f(x+h)-_f(x-h))/(2.0*h);
}

//метод деления интервала пополам
tuple<double, int> alg_132_Metod_Delenai_Intervala_Popalam(double a, double b, const double &e)
{
    std::cout << __func__ << ": " << std::endl;
    int it = 0;
    while(fabs(b-a) > e)
    {
        double xi = (b+a)/2.0;
        
        if (f(a) <= f(xi))
        {
            b = xi;
        } else { a = xi; }
        ++it;
    }
    return make_tuple((b+a)/2, it);
}
// метод дихотомии
tuple<double, int> alg_133_Metod_Dihotomii(double a, double b, const double &e)
{
    std::cout << __func__ << ": " << std::endl;
    int it = 0;
    double g = e * 0.001;

    while(fabs(b-a) > e)
    {
        double xi = (b+a)/2;
        
        if (f(xi-g) <= f(xi+g))
        {
            b = xi+g;
        } else { a = xi-g; }
        ++it;
    }
    return make_tuple((b+a)/2, it);
}
// метод золотого сечения
tuple<double, int> alg_134_Metod_Zolotogo_Sechenia(double a, double b, const double &e)
{
    std::cout << __func__ << ": " << std::endl;
    int it = 0;
    double l = 1.618033989;

    double xi = 0;
    double x1, x2, y1, y2;
    while(fabs(b-a) > e)
    {
        x1 = b-(b-a)/l;
        x2 = a+(b-a)/l;
        
        y1 = f(x1);
        y2 = f(x2);

        if (f(x1) <= f(x2))
        {
            b = x2;
            x2 = x1;
            y2 = y1;
            x1 = a+b-x2;
            y1 = f(x1);
        } else
        {
            a = x1;
            x1 = x2;
            y1 = y2;
            x2 = a+b-x1;
            y2 = f(x2);
        }
        ++it;
    }
    if (y1 < y2)
    {
        xi = x1;
    } else { xi = x2; }
    return make_tuple(xi, it);
}

//метод касательных
tuple<double, int> alg_141_Metod_Kasatelnoi(double a, double b, const double &e)
{
    std::cout << __func__ << ": " << std::endl;
    int it = 0;
    double xi = 0, c = 0;
    double z, y;
    double y1 = f(a), y2 = f(b);
    double z1 = diff(a, f), z2 = diff(b, f);

    while(fabs(b-a) > e)
    {
        c = ((b*z2 - a*z1) - (y2 - y1)) / (z2 - z1);

        y = f(c);
        z = diff(c, f);
        if (z == 0)
        {
            xi = c;
            break;
        } else if (z < 0)
        {
            a = c;
            y1 = y;
            z1 = z;
        } else
        {
            b = c;
            y2 = y;
            z2 = z;
        }
        xi = (b+a)/2;

        ++it;
    }
    return make_tuple(xi, it);
}
//метод парабол
tuple<double, int> alg_142_Metod_Parabol(double a, double b, const double &e)
{
    std::cout << __func__ << ": " << std::endl;
    int it = 0;
    double xi = 0;

    double c = a+(b-a)/2;
    double y, ya = f(a), yb = f(b), yc = f(c);
        
    while(fabs(b-a) > e)
    {
        double t = c + 0.5*(pow(b-c, 2)*(ya-yc) - pow(c-a, 2)*(yb-yc))/((b-c)*(ya-yc) + (c-a)*(yb - yc));

        if (t == c)
        {
            xi = (a+c)/2;
        } else { xi = t; }
        y = f(xi);

        if (xi < c)
        {
            if (y < yc)
            {
                b = c;
                c = xi;
                yb = yc;
                yc = y;
            } else if (y > yc)
            {
                a = xi;
                ya = y;
            } else
            {
                a = xi;
                b = c;
                c = (xi+c)/2;
                ya = y;
                yb = yc;
                yc = f(c);
            }
        } else if (xi > c)
        {
            if (y < yc)
            {
                a = c;
                c = xi;
                ya = yc;
                yc = y;
            } else if (y > yc)
            {
                b = xi;
                yb = y;
            } else
            {
                a = c;
                b = xi;
                c = (xi+c)/2;
                ya = yc;
                yb = y;
                yc = f(c);
            }
        }
        ++it;
    }
    return make_tuple(xi, it);
}

int main(int, char**)
{
    double a = 0.0, b = 2.0;
    double e = 0.0015;

    tuple<double, int> (*func[5])(double, double, const double&);

    func[0] = alg_132_Metod_Delenai_Intervala_Popalam;
    func[1] = alg_133_Metod_Dihotomii;
    func[2] = alg_134_Metod_Zolotogo_Sechenia;
    func[3] = alg_141_Metod_Kasatelnoi;
    func[4] = alg_142_Metod_Parabol;

    vector<int> min_it, max_it;

    double x;
    int it;
    int min = numeric_limits<int>::max();
    int max = numeric_limits<int>::min();
    for (int i = 0; i<5; ++i)
    {
        cout << i+1 << ". ";

        std::tie(x, it) = func[i](a, b, e);

        cout << "\tРезультат:";
        cout << "\n\t  x: " << x;
        cout << "\n\t  y: " << f(x);
        cout << "\n\tКоличество экспериментов: "  << it << endl;

        if (it == max) { max_it.push_back(i+1); }
        if (it > max)
        {
            max = it;
            max_it = {i+1};
        }

        if (it == min) { min_it.push_back(i+1); }
        if (it < min)
        {
            min = it;
            min_it = {i+1};
        }
    }
    
    cout << "\nВывод:";
    cout << "\n\tМинимальное количество итераций: " << min;
    cout << "\n\t  Самые быстрые алгоритмы: ";
    for(auto iter=min_it.begin(); iter!=min_it.end(); ++iter) { std::cout << *iter << ' '; }
    cout << "\n\tМаксимальное количество итераций: " << max;
    cout << "\n\t  Самые долгие алгоритмы: ";
    for(auto iter=max_it.begin(); iter!=max_it.end(); ++iter) { std::cout << *iter << ' '; }
    cout << endl;

}
