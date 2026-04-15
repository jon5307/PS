#include <iostream>
#include <string>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    float unit, grade_score, sum_score = 0;
    int c = 0;
    string subject, grade;

    while (1)
    {
        cin >> subject >> unit >> grade;
        if (cin.eof())
            break;

        if (grade.compare("A+") == 0)
            grade_score = 4.5;
        else if (grade.compare("A0") == 0)
            grade_score = 4.0;
        else if (grade.compare("B+") == 0)
            grade_score = 3.5;
        else if (grade.compare("B0") == 0)
            grade_score = 3.0;
        else if (grade.compare("C+") == 0)
            grade_score = 2.5;
        else if (grade.compare("C0") == 0)
            grade_score = 2.0;
        else if (grade.compare("D+") == 0)
            grade_score = 1.5;
        else if (grade.compare("D0") == 0)
            grade_score = 1.0;
        else if (grade.compare("F") == 0)
            grade_score = 0.0;
        else
            continue;

        c += unit;
        sum_score += unit * grade_score;
    }

    cout << sum_score / c; 
    return 0;
}
