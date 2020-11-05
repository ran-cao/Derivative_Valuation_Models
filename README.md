# Derivative_Valuation_Models
Compare three models (1) Binomial Tree model (2) Monte-Carlo Simulation (3) Analytic Model, i.e. the Black-Scholes formula using European put option and American put option

### Situation and goals
When we think about financial derivative, we usually hope to be able to figure out its value prior to expiration or settlement date𝑇. In order to evaluate the financial derivative price, we describe its value as a function of the underlying asset price and time.

In this project, we seek to demonstrate three primary derivative valuation approaches that we have talked about in class: (1) Binomial Tree model, (2) Monte-Carlo Simulation, and (3) Analytic Model, i.e. the Black-Scholes formula. We aim to illustrate and analyze the convergence of these three approaches through a European put option. We study the convergence pattern of the Binomial Tree method with different number of steps or paths, ranging from 30 to 39, then 300 to 309. In addition, we construct a histogram of the Monte-Carlo Simulation simulated price and perform statistical analysis to show the statistical properties of these simulated price. We then compare how fast the Binomial Tree method converges and how good the Monte-Carlo simulation method is, using the number calculated using the Black-Scholes formula as a benchmark.

Additionally, we also show and compare the value of an American put option with that of a European put option that has the same parameters.

### Hypothesis and expected results
For the Binomial Tree method, we expect the result to be closer to the true value calculated by the Black-Scholes formula as the number of steps increases. This means that the difference between the price given by the Binomial Tree model and the price calculated by the Black-Scholes formula decreases as the number of steps increases, so the Binomial Tree model prices converge to the Black-Scholes price.

For the Monte-Carlo Simulation, we hypothesize that the more times we run the simulations, i.e. the higher our number of observations for the price and the smaller our confidence interval for the true value of the put option price is. This means that if we keep running the simulation multiple times, eventually, we will likely be confident enough to say that the price produced by our simulation is not different from the price calculated by the Black-Scholes formula.


### Conclusion
Through this project, we conclude that all three approaches of pricing a European put option converge and give us the very similar results. The put option value ranges from 2.7892 to 2.7904 using the Binomial Tree model with around 300 steps, and from 2.7638 to 2.8155 using the Monte-Carlo simulation with 10,000 trajectories. The Black-Scholes formula gives us a value of 2.79, which falls into the range of both the Binomial Tree model and the Monte-Carlo simulation.
Additionally, as the number of steps increases for the Binomial Tree model, the put option value gets closer and closer to 2.79, the value given by the Black-Scholes formula. On a similar note, the statistical analysis shows the Monte-Carlo simulation also converges to 2.79.

### Further
We examine the relationship between the European put price and the parameters that define the option, such as time to maturity, 𝑇, strike price, 𝐾, interest rate, 𝑟, and volatility, 𝜎. We find: European put price is positively related to the time to maturity, 𝑇, the strike price, 𝐾, and the volatility, 𝜎. However, it is negatively related to the risk-free interest rate, 𝑟!.
