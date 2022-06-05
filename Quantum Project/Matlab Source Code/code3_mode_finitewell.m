%Atilla Ozgur Cakmak
%Calculating bound modes inside the finite well
%The user enters the beta value for the potential well and the plots show
%how many crossings are created as a result. 
clear all
clc
% close all

%constants
m=9.1e-31; %mass of electron
h=6.626e-34; %Planck's constant

%variables
beta=input('Enter beta: '); %beta constant of the rectangular potential
k_pa=[0:5*pi/1000:5*pi]; %wavevector times well width gives us a dimensionless variable

%equations
eq1=sqrt(beta^2-k_pa.^2)./k_pa;  %red
eq2=-k_pa./sqrt(beta^2-k_pa.^2); %green
eq3=tan(k_pa);

%plotting
figure
plot(k_pa,eq1,'r','LineWidth',3)
hold
plot(k_pa,eq2,'g','LineWidth',3)
plot(k_pa,eq3,'LineWidth',3)
ylim([-10 10])
xlabel('k_pa')
%grid on
title('Intersect with the Blue Curve and Find the Modes');
legend('Even Modes','Odd Modes');
set(gca,'fontsize',12,'fontweight','bold')

syms x;
even=input('red(1) or green(0) curve?: ');
if even==1
    eqnLeft=sqrt(beta^2-x^2)./x;
else
    eqnLeft=-x/sqrt(beta^2-x^2);
end
eqnRight=tan(x);
vicinity=input('enter vicinity of kpa(try to choose a guessing point that will be away from the next solution): ');
display('if an error occurs, choose a better guess in the vicinity of the kpa to find the mode');
k_pa=vpasolve(eqnLeft==eqnRight,x,vicinity);
%user enters whether the mode is even or not based on k_pa crossing
%eg. n=1 is even, first crossing is even

%calculation of the mode
V0=input('enter V0 potential of the well in eV (negative potential): ')*1.6e-19;
E_over_V0=(beta^2-k_pa^2)/beta^2;
E=V0*E_over_V0;
a=beta*h/(2*pi)/sqrt(2*m*abs(V0)); %sorting out the thickness of the potential
k=sqrt(2*m*E)*2*pi/h;
k_p=sqrt(2*m*(E-V0))*2*pi/h;
x_range=input('enter x range in a (positive number from -x_range*a to x_range*a): ');
x=[-x_range*a:4*a/100:x_range*a];
C=1;
F=(k_p+k)*exp(i*(k-k_p)*a)/(2*k_p)*C;
G=(k_p-k)*exp(i*(k+k_p)*a)/(2*k_p)*C;
M12=i/2*(k_p/k-k/k_p)*sin(2*k_p*a);
B=C/M12; %A=0

    Psi_L=B*exp(-i*k*x);
    Psi_I=F*exp(i*k_p*x)+G*exp(-i*k_p*x);
    Psi_R=C*exp(i*k*x);
    [temp,index1]=min(abs(x+a));
    [temp,index2]=min(abs(x-a));
    Psi(1:index1)=Psi_L(1:index1);
    Psi(index1+1:index2)=Psi_I(index1+1:index2);
    Psi(index2+1:length(x))=Psi_R(index2+1:length(x));
    %taking numerical integral with Simpson's rule
    integ=0;
    for iii=2:length(Psi)-1
        if mod(iii,2)==1
            integ=integ+4*abs(Psi(iii))^2;
        else
            integ=integ+2*abs(Psi(iii))^2;
        end
    end
    integ_total=(integ+abs(Psi(1))^2+abs(Psi(length(Psi)))^2)*4*a/100*1/3; %integral dx should be same as x resolution
    %integ_total(ii)=trapz(x,abs(Psi(ii,:)).^2);
    Psi=Psi/integ_total;
for i=1:length(x)
    well_L(i)=-a;
    well_R(i)=a;
end
figure
plot(x*1e9,Psi,'LineWidth',3)
hold
plot(well_L*1e9,[-1:2/(length(x)-1):1]*max(Psi),':k','LineWidth',5); %well borders -5 to 5 taken
plot(well_R*1e9,[-1:2/(length(x)-1):1]*max(Psi),':k','LineWidth',5);
legend(['E=' num2str(double(E/1.6e-19)) 'eV in V_0 of ' num2str(double(V0/1.6e-19)) 'eV, a=' num2str(a*1e9) 'nm'])
title('Mode in a Finite Well from -a to a');
xlabel('position x (nm)');
ylabel('Amplitude');
axis tight;
grid on;
set(gca,'fontsize',16,'fontweight','bold')

            
    
    
    
    
