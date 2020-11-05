S0=60
r=0.05
b=0.15
T=0.5
m=10000
n=10000
K=rep(62,m)
deltaT=T/n
#record the path at discrete n values as a vector S and m path’s ending price as a vector Y
S=rep(S0,n+1)
Y=rep(0,m)
#record m path’s
start_time <-Sys.time()
for(j in 1:m)
{
  W=rnorm(n,0,1)
  for(i in 1:n)
  {
    S[i+1]=S[i]+r*S[i]*deltaT+ b*S[i]*sqrt(deltaT)*W[i]
  }
  Y[j]=S[n+1]
  D[j]=max(K[j]-Y[j],0)
}
p=exp(-r*T)*mean(D)
p
end_time<-Sys.time()
end_time-start_time

#After we ran 10 times, we drew the put prices in a histogram
put <-c(2.791445,2.775245,2.788279,2.770456,2.750464,2.751529,2.821298,2.858014,2.759759,2.830136)
hist(put)
mean(put)
sd(put)

# computing time 
time<-c(3.538606,2.098537,2.16416,2.304429,2.254412,2.160703,2.176784,2.204395,2.215259,2.433899)
hist(time)
mean(time)
sd(time)

# Used Black Scholes as a benchmark and conducted a one sample t-test
black_scholes = 2.79
t.test(put-black_scholes)

# n =300, find the computing time
n = 300
start_time <-Sys.time()
for(j in 1:m)
{
  W=rnorm(n,0,1)
  for(i in 1:n)
  {
    S[i+1]=S[i]+r*S[i]*deltaT+ b*S[i]*sqrt(deltaT)*W[i]
  }
  Y[j]=S[n+1]
  D[j]=max(K[j]-Y[j],0)
}
p=exp(-r*T)*mean(D)
p
end_time<-Sys.time()
end_time-start_time

time_n_300<-c(3.89943, 3.821827, 3.826226,4.637946,4.83352,4.109647,3.734435,3.712343,3.733233,3.673538)
hist(time_n_300)
mean(time_n_300)
sd(time_n_300)