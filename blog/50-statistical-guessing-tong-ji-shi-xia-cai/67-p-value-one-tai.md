# ❖ P-value (One-tailed)

> _p-value_ stands for "probability value", which is the **most confusing concept** in Hypothesis testing. So it's necessary to pick it out here before exceeding to the Significance Testing.

[Refer to youtube: Hypothesis Testing 5: p values (one sample t test)](https://www.youtube.com/watch?v=WojcyhC7EVc)

**_p-value_ tells the MAXIMUM of the "truth" takes part in your story.**

> The smaller the true part (_p-value_) in the story, the greater the evidence against the story(_null hypothesis_).

For example, you said your IQ is 130. So we build a **MODEL** based on your claim. And then we ask you to take a real IQ test which tells your IQ is 117. So the calculation tells that the **REAL** part only takes **utmost 0.47%** in your "story". Therefore, if there is only less than 0.47% truth in a story, we can claim the story is a **LIE**! And 0.47% is the `p-value`.

![image](https://user-images.githubusercontent.com/14041622/45283471-8e853980-b510-11e8-8207-5f50e8ed33dd.png)


## Steps to calculate 「p-value」

- First we assume the story (__null hypothesis__) is **true**,
- and we do a large number of simulations based on the story **to form a normal distribution**,
- then we take a **real sample**, 
- draw the sample data onto the **hypothesis distribution**,
- calculate how much proportion it is **from the sample data to a tail**,
- if it's not told `left-tail` or `right-tail`, then the proportion is **two-tails** adding up together.
- And that proportion is the `p-value`, as the **utmost probability of the true story in hypothesis**.

![image](https://user-images.githubusercontent.com/14041622/45207840-b62f9400-b2bb-11e8-9ea6-87b7dd1c69de.png)


## p-value from 「Discrete Distribution」

Just to **count** how many _outcomes_ are **"further"** than the _sample data_ to the mean, divided by the total outcomes.

![image](https://user-images.githubusercontent.com/14041622/45283032-503b4a80-b50f-11e8-8ae2-e0e4074c72d6.png)


### Example
![image](https://user-images.githubusercontent.com/14041622/45252474-82bb3b00-b389-11e8-8062-df8e230d202c.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/45253091-d468c300-b393-11e8-8ab4-e8d69c4925ff.png)


### Example
![image](https://user-images.githubusercontent.com/14041622/45253139-b2bc0b80-b394-11e8-9282-d693cc1dd252.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/45253143-be0f3700-b394-11e8-9545-4f9bbb15a069.png)


## p-value from 「Continuous Distribution」





## p-value is a  「Conditional Probability」

[`▶︎ Jump back to previous note: Conditional Probability`](https://github.com/solomonxie/solomonxie.github.io/issues/50#issuecomment-412445737)

![image](https://user-images.githubusercontent.com/14041622/45284577-7cf16100-b513-11e8-9c09-bc6aa0ae08d2.png)

![image](https://user-images.githubusercontent.com/14041622/45284498-529fa380-b513-11e8-927e-8fb15a5899de.png)

