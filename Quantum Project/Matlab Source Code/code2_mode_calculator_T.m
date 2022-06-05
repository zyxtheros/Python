%Atilla Ozgur Cakmak
%Calculating modes inside wells and barriers in order to find the
%transmission coefficient. The user enters beta value and E/V0 gets T
clear all
clc

%constants
m=9.1e-31; %mass of electron
h=6.626e-34; %Planck's constant

%variables
E=1*1.6e-19; %energy of the incoming electron
beta=10; %beta constant of the rectangular potential
E_over_V0=input('Enter your E over V0 value'); %E_over_V0 is entered by the user
A=1; %incoming wavefunction

%definitions
V0=E/E_over_V0;
a=beta*h/(2*pi)/sqrt(2*m*abs(V0)); %sorting out the thickness of the potential
k=sqrt(2*m*E)*2*pi/h; %outside the potential wavefunction
k_p=sqrt(2*m*(E-V0))*2*pi/h; %inside the potential wavefunction

%calculating B, C, F and G coefficients from TMM formulation
M11=cos(2*k_p*a)+i/2*(k/k_p+k_p/k)*sin(2*k_p*a);
M12=i/2*(k_p/k-k/k_p)*sin(2*k_p*a);
M21=conj(M12);
M22=conj(M11);

B=-M21*A*exp(-2*i*k*a)/M22;
C=(M11*A*exp(-i*k*a)+M12*B*exp(i*k*a))*exp(-i*k*a);
F=(k_p+k)*exp(i*(k-k_p)*a)/(2*k_p)*C;
G=(k_p-k)*exp(i*(k+k_p)*a)/(2*k_p)*C;

%plotting modes
x=[-5*a:4*a/1000:5*a];
Psi_L=(A*exp(i*k*x)+B*exp(-i*k*x)); 
Psi_I=(F*exp(i*k_p*x)+G*exp(-i*k_p*x));
Psi_R=(C*exp(i*k*x));

for ii=1:length(x)
    if x(ii) <= -a
        Psi(ii)=Psi_L(ii);
    elseif x(ii) <=a
        Psi(ii)=Psi_I(ii);
    elseif x(ii)> a
        Psi(ii)=Psi_R(ii);
    end
    well_L(ii)=-1;
    well_R(ii)=1;
end
subplot(2,1,2)
yyaxis left;
plot(x/a,real(Psi),'LineWidth',3)
hold
plot(x/a,imag(Psi),'r','LineWidth',3)
yyaxis right;
plot(x/a,abs(Psi).^2,':k','LineWidth',3)
plot(well_L,-5:10/(length(x)-1):5,'--k','LineWidth',5); %well borders -5 to 5 taken
plot(well_R,-5:10/(length(x)-1):5,'--k','LineWidth',5);
annotation('rectangle',[0.2 .3 .1 .1],'FaceColor','white','FaceAlpha',1);
annotation('textbox',[0.2 .3 .1 .1],'String',['\beta= ' num2str(beta)],'FitBoxToText','on','FontSize',16);
annotation('rectangle',[0.2 .5 .1 .1],'FaceColor','white','FaceAlpha',1);
annotation('textbox',[0.2 .5 .1 .1],'String',['E/V_0= ' num2str(E_over_V0)],'FitBoxToText','on','FontSize',16);
grid on
title('Electron Wave Interacting with the Potential Located from x=-a to a');
legend('Real{\Psi} e^- wave','Imag{\Psi} e^- wave','|\Psi| e^- wave');
xlabel('position (x/a)')
ylabel('Amplitude');
set(gca,'fontsize',16,'fontweight','bold')
        

