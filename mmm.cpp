#include <string.h>
#include <fstream>

#define g 9.8145

double f_rk(double v, double m, double b)
{
    double v_n=-g+b*v/m;
    return v_n;
}

int main(int argc, char** argv)
{
    std::fstream wyniki;
    wyniki.open("wyniki.csv",std::fstream::out);
    printf("%s",argv[0]);
    const double m = atof(argv[1]);
    const double b = atof(argv[2]);
    const double y0 = atof(argv[3]);
    const double H = atof(argv[4]);
    //const double v0 = atof(argv[5]);
    
    int i=0;
    double y=y0;
    double v=0;
    double t=0;

    double k1_v=0, k2_v=0, k3_v=0, k4_v=0;
    double k1_y=0, k2_y=0, k3_y=0, k4_y=0;

    do
    {

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
        if (y<0) y=0;
        wyniki<<t<<" ;"<<y<<" ;"<<v<<'\n';
        t+=H;
    }while(y>0);
wyniki.close();
return 0;
}