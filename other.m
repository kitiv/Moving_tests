
%% 

% Пики на угле Y. pcs - начало dpcs - конец переноса стопы
bb=(ang(x(1):x(2),3)-ang(x(1),3))/max(ang(x(1):x(2),3));
H=0.6;
D=15;
H1=0.4;
D1=20
% [dpcs1,dpcs]=findpeaks( -bb.*(bb<0),'MinPeakHeight',H1,'MinPeakDistance',D1);
% [pcs1,pcs]=findpeaks( bb,'MinPeakHeight',H,'MinPeakDistance',D );
findpeaks( bb,'MinPeakHeight',H,'MinPeakDistance',D); hold on
% findpeaks( -bb.*(bb<0),'MinPeakHeight',0.4,'MinPeakDistance',20);
% figure; plot(bb); hold on; plot(pcs,pcs1,'o'); plot(dpcs,-dpcs1,'o')
%% 
ab=(ang_vel(x(1):x(2),3)-ang_vel(x(1),3))/max(ang_vel(x(1):x(2),3));
ab1=-ab.*(ab<0)
H=0.2;
D=10;
[vpcs1,vpcs]=findpeaks( ab1 ,'MinPeakHeight',H,'MinPeakDistance',D );
findpeaks( ab1,'MinPeakHeight',H,'MinPeakDistance',D);
% figure; plot(ab); hold on; plot(vpcs,-vpcs1,'o'); 
%% 
figure; plot(ab); hold on; plot(vpcs,-vpcs1,'o'); plot(pcs,pcs1./pcs1-1,'o'); plot(dpcs,-dpcs1./dpcs1+1,'o'); 
 

%% 
% pcs=pcs+x(1);
p1=length(pcs);
dl=15;%pcs(3)-pcs(2)+x(1);
for i=1:p1
    p(1,i,:)=acc(pcs(i)-dl:pcs(i)+dl,1);
    p(2,i,:)=acc(pcs(i)-dl:pcs(i)+dl,2);
    p(3,i,:)=acc(pcs(i)-dl:pcs(i)+dl,3);
    p(4,i,:)=ang_vel(pcs(i)-dl:pcs(i)+dl,1);
    p(5,i,:)=ang_vel(pcs(i)-dl:pcs(i)+dl,2);
    p(6,i,:)=ang_vel(pcs(i)-dl:pcs(i)+dl,3);
    p(7,i,:)=ang(pcs(i)-dl:pcs(i)+dl,1);
    p(8,i,:)=ang(pcs(i)-dl:pcs(i)+dl,2);
    p(9,i,:)=ang(pcs(i)-dl:pcs(i)+dl,3);
    p(10,i,:)=mag(pcs(i)-dl:pcs(i)+dl,1);
    p(11,i,:)=mag(pcs(i)-dl:pcs(i)+dl,2);
    p(12,i,:)=mag(pcs(i)-dl:pcs(i)+dl,3);
    p(13,i,:)=qatern(pcs(i)-dl:pcs(i)+dl,1);
    p(14,i,:)=qatern(pcs(i)-dl:pcs(i)+dl,2);
    p(15,i,:)=qatern(pcs(i)-dl:pcs(i)+dl,3);
    p(16,i,:)=qatern(pcs(i)-dl:pcs(i)+dl,4);
end
%% 
dem={'a_x','a_y','a_z','v_x','v_y','v_z','ang_x','ang_y','ang_z','m_x','m_y','m_z','q_1','q_2','q_3','q_4'};
for i=1:16
    figure;
    b(:,:)=p(i,:,:);
    imagesc(b); shading interp
    title(dem(i))
end
%% 
for i=1:p1-1
    time_step(i)=pcs(i+1)-pcs(i);
end
figure;
plot(time_step);
%% 
dem={'a_x','a_y','a_z','v_x','v_y','v_z','ang_x','ang_y','ang_z','m_x','m_y','m_z','','','','','q_1','q_2','q_3','q_4'};
for i=[1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20] 
%     figure;    
    plot((Incl(x(1):x(2),i)-Incl(x(1),i))/max(Incl(x(1):x(2),i))+i); hold on
    title(dem(i))
end
%% 
a=ang_vel(x(1):x(2),1);
p=(abs(a)<15);
p(1)=1; p(end)=1; p(2)=1; p(end-1)=1;
p1=p;
for i=3:length(p)-2
    Sum=p(i)+p(i-1)+p(i+1)+p(i+2)+ p(i-2);
    if Sum<3
        p1(i)=0;
    end
end    
%% 
plot((diff(p1))*200); hold on; plot(a)

