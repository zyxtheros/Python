%Atilla Ozgur Cakmak
%Calculating transmission coefficient
clear all
clc
close all

%constants
m=9.1e-31; %mass of electron
h=6.626e-34; %Planck's constant

%variables
E=1*1.6e-19; %energy of the incoming electron 
E_over_V0=[-5:0.0001:5]; %it is critical to define E/Vo first to avoid singularities 
V0=E./E_over_V0; %energy level of the rectangular potential
beta=input('Enter beta value (must be bigger than 0): '); %beta constant of the rectangular potential
a=beta*h/(2*pi)./sqrt(2*m*abs(V0)); %sorting out the thickness of the potential

%calculating the transmission coefficient (T)
k=sqrt(2*m*E)*2*pi/h; %free space wave vector
k_p=sqrt(2*m*(E-V0))*2*pi/h; %k' wave vector inside the rectangular potential 
T=abs(1./(1+1/4*((k./k_p-k_p/k).^2).*(sin(2*k_p.*a)).^2)); 
figure;
plot(E_over_V0,T,'LineWidth',3)
grid on
title('Electron Interacting with the Potential');
legend(['\beta= ' num2str(beta)])
xlabel('E/V_0 (Electron Energy over Potential Energy)')
ylabel('Transmission')
set(gca,'fontsize',16,'fontweight','bold')

