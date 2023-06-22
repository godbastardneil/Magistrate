#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

const double dx = 1e-8;

double func(const vector <double> &x)
{
    return (x[0]-2)*(x[0]-2)+(x[1]-5)*(x[1]-5);
}
double func(const double &x1, const double &x2)
{
    return (x1-2)*(x1-2)+(x2-5)*(x2-5);
}
vector<double> dxdy(const vector <double> &x)
{
    return {(func(x[0]+dx, x[1]) - func(x))/dx,
            (func(x[0], x[1]+dx) - func(x))/dx};
}

int main()
{
    //Градиентный метод с постоянным шагом
    vector<double> x = {0, 2};
    const double eps = 0.0001, alpha = 0.1;
    cout << "Значение в первой базисной точке: func(x) = func(" << x[0] << "; " << x[1] << ") = " << func(x) << endl;

    vector<double> _dxdy = dxdy(x);
    cout << "Вектор-градиент = (" << _dxdy[0] << ", " << _dxdy[1] << ")" << endl;
    double grad = sqrt(_dxdy[0]*_dxdy[0] + _dxdy[1]*_dxdy[1]);
    cout << "\tГрадиента = " << grad << endl;

    for (int i = 0; i < 1000 && grad > eps; ++i)
    {
        cout << endl << "Итерация " << i << endl;

        x = {x[0] - alpha*_dxdy[0], x[1] - alpha*_dxdy[1]};
        cout << "\tЗначение в новой базисной точке: func(xk) = func(" << x[0] << "; " << x[1] << ") = " << func(x) << endl;

        _dxdy = dxdy(x);
        cout << "\tВектор-градиент = (" << _dxdy[0] << ", " << _dxdy[1] << ")" << endl;
        grad = sqrt(_dxdy[0]*_dxdy[0] + _dxdy[1]*_dxdy[1]);
        cout << "\tГрадиента = " << grad << endl;
    }
    cout << "Решение - f(" << x[0] << ", " << x[1] << ") = " << func(x) << endl;
    return 0;
}