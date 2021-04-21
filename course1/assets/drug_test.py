def drug_user(prob_theta = 0.5,
              sensitivity = 0.97,
              specificity = 0.95,
              prevalence = 0.01,
              verbose = True):
    """Compute the posterior using the Bayes' rule.
    Verbose is a general programming term for produce lots of logging output.
    You can think of it as asking the program to "tell me everything about what you are doing all the time".
    Just set it to true and see what happens."""

    p_user = prevalence
    p_non_user = 1 - prevalence
    p_positive_user = sensitivity
    p_negative_non_user = specificity
    p_positive_non_user = 1 - specificity

    num = p_positive_user * p_user
    den = p_positive_user * p_user + p_positive_non_user * p_non_user

    prob = num/den

    if verbose:
        if prob > prob_theta:
            print("The test-taker could be a drug user.")

        else:
            print("The test-taker may not be a drug user.")
    return prob

p = drug_user(prob_theta = 0.5,
              sensitivity = 0.97,
              specificity = 0.95,
              prevalence = 0.01)

print("Probability of the test-taker being a drug user is:", round(p,3))


ps = []
pres = []
for pre in [i*0.001 for i in range(1,51,2)]:
    pres.append(pre*100)
    p = drug_user(prob_theta = 0.5,
                  sensitivity = 0.97,
                  specificity = 0.95,
                  prevalence = 0.01,
                  verbose = False)
    ps.append(p)
import seaborn as sns

sns.lineplot(pres, ps)
