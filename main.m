%% ЗАгрузка данных, определение рабочей области.

clear all
name='D:\Downloads\WT901WIFI\WT901WIFI\WIFI software-UDP mode pairing network\data\20200402\18.log'%'C:\Users\Александр\Desktop\23.log';
Incl=importdata(name,',');
Incl1=importdata(name,' ');
txt=Incl.textdata;
Incl=Incl.data;
% Incl1=Incl1.data;
% for i =1:20
%     Incl(:,i)=interp1(1:length(Incl1(:,1)),Incl1(:,i),1:1/2:length(Incl1(:,1)),'spline');
% end
acc=Incl(:,[1,2,3]); 
mag=Incl(:,[10,11,12]); 
ang_vel=Incl(:,[4:6]);
ang=Incl(:,[7,8,9]);
qatern=Incl(:,[17:20]);
figure;
plot(ang_vel(:,2))
[x,y] = ginput(2);
x=fix(x);
close;
%% Определение начала 1й 5й фаз 
%Выделение плато из ang_v_x
dx=20;
a=ang_vel(x(1):x(2),1);
p=(abs(a)<dx);
p(1)=1; p(end)=1; p(2)=1; p(end-1)=1;


for i=3:length(p)-2
    Sum=p(i)+p(i-1)+p(i+1)+p(i+2)+p(i-2);%+p(i+3)+p(i-3)+p(i+4)+p(i-4);
    if Sum<3
        p(i)=0;
    else
        p(i)=1;
    end
end 
[p1y,p1]=findpeaks( -diff(p),'MinPeakHeight',0.5,'MinPeakDistance',10);
[p5y,p5]=findpeaks( diff(p),'MinPeakHeight',0.5,'MinPeakDistance',10);
p5=p5+1;
figure; plot(a); hold on; plot(p1,p1y,'o'); plot(p5,p5y,'o')

%% Определение начала 2 фазы

aa=ang(x(1):x(2),1);
H=0.6;
D=25;
[p2y,p2]=findpeaks( -smooth(diff(a)),'MinPeakHeight',H,'MinPeakDistance',D);
figure; plot(aa); hold on; plot(p2,p2y/2,'o');

%% Определение начала 3 фазы

H=20;
D=25;
[p3y,p3]=findpeaks((-a),'MinPeakHeight',H,'MinPeakDistance',D);
figure; plot(a); hold on; plot(p3,-p3y,'o');


%% Определение начала 4 фазы

ab=acc(x(1):x(2),3)-acc(x(1),3);
H=0.1;
D=25;
[p4y,p4]=findpeaks(-ab,'MinPeakHeight',H,'MinPeakDistance',D);
figure; plot(ab); hold on; plot(p4,-p4y,'o');
%% 

figure; plot(a); hold on; plot(p1,p1y*0,'o'); plot(p2,p2y*0,'*'); plot(p3,-p3y*0,'*'); plot(p4,-p4y*0,'o'); plot(p5,-p5y*0,'o');

%% Построение гистограмм фаз

for i=1:length(p1)-1
    step_time(i)=p1(i+1)-p1(i);
    phase_time(5,i)=p1(i+1)-p5(i);
end


for i=1:length(p1)
    phase_time(1,i)=p2(i)-p1(i);
    phase_time(2,i)=p3(i)-p2(i);
    phase_time(3,i)=p4(i)-p3(i);
    phase_time(4,i)=p5(i)-p4(i);
end

figure;hold on;
for i=1:5
 plot(phase_time(i,:),'-o')
end
hold off

figure; hist(phase_time(1,:)); title(['Phase 1 ','std=',num2str(std(phase_time(1,:))),' mean=',num2str(mean(phase_time(1,:)))]);
figure; hist(phase_time(2,:)); title(['Phase 2 ','std=',num2str(std(phase_time(2,:))),' mean=',num2str(mean(phase_time(2,:)))]);
figure; hist(phase_time(3,:)); title(['Phase 3 ','std=',num2str(std(phase_time(3,:))),' mean=',num2str(mean(phase_time(3,:)))]);
figure; hist(phase_time(4,:)); title(['Phase 4 ','std=',num2str(std(phase_time(4,:))),' mean=',num2str(mean(phase_time(4,:)))]);
figure; hist(phase_time(5,:)); title(['Phase 5 ','std=',num2str(std(phase_time(5,:))),' mean=',num2str(mean(phase_time(5,:)))]);
figure; hist(step_time); title(['Step ','std=',num2str(std(step_time(:))),' mean=',num2str(mean(step_time(:)))]);

%% Визуализация шагови фаз
figure; hold on;
for i = 1:length(p1)-1
    plot(a(p1(i):p1(i+1)));    
end
hold off;

figure; hold on;
for i = 1:length(p1)
    plot(a(p1(i):p2(i)));    
end
hold off;

figure; hold on;
for i = 1:length(p1)
    plot(a(p2(i):p4(i)));    
end
hold off;


figure; hold on;
for i = 1:length(p1)
    plot(a(p4(i):p5(i)));    
end
hold off;

figure; hold on;
for i = 1:length(p1)-1
    plot(a(p5(i):p1(i+1)));    
end
hold off;
