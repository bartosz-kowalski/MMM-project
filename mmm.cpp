#include <string.h>
#include <fstream>
#include <math.h>

#define g 9.8145
#define h 8000

int sgn(double v)
{
    if(v<0)
        return -1;
    else if(v==0)
        return 0;
    else
        return 1;
}

double f_rk(double v, const double m, double& b)
{
    double v_n=-g-b*v*v/m*sgn(v);
    return v_n;
}

void b_increase(double& b, const double y)
{
    b*=exp(-y/h);
}

int main(int argc, char** argv)
{
    std::fstream wyniki;
    wyniki.open("wyniki.csv",std::fstream::out);
    printf("%s",argv[0]);
    const double m = atof(argv[1]);
    double b = atof(argv[2]);
    const double y0 = atof(argv[3]);
    const double H = atof(argv[4]);
    const double v0 = atof(argv[5]);
    
    int i=0;
    double y=y0;
    double v=v0;
    double v_old=v;
    double a = -g;
    double t=0;

    double k1_v=0, k2_v=0, k3_v=0, k4_v=0;
    double k1_y=0, k2_y=0, k3_y=0, k4_y=0;

    do
    {
        v_old=v;
        k1_y=H*v;
        k1_v=H*f_rk(v,m,b);

        k2_y=H*(v+k1_y/2);
        k2_v=H*f_rk(v+k1_v/2,m,b);

        k3_y=H*(v+k2_y/2);
        k3_v=H*f_rk(v+k2_v/2,m,b);

        k4_y=H*(v+k3_y);
        k4_v=H*f_rk(v+k3_v,m,b);

        y+=(k1_y+2*k2_y+2*k3_y+k4_y)/6;
        v+=(k1_v+2*k2_v+2*k3_v+k4_v)/6;
        a=(v-v_old)/H;
        if (y<0) y=0;
        wyniki<<t<<" ;"<<y<<" ;"<<v<<" ;"<<a<<'\n';//<<" ;"<<b
        t+=H;
        //b_increase(b,y);
    }while(y>0);
wyniki.close();
return 0;
}
