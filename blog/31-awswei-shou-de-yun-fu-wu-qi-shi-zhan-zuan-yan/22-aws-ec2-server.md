# ❖ 「AWS EC2」Server Overview [DRAFT]


## 「PRICING」

`On-Demand instances`, you pay for compute capacity by per hour or per second depending on which instances you run.
`Spot instances` are available at a **discount** of up to 90% off compared to On-Demand pricing.
`Reserved Instances` provide you with a significant discount (up to 75%) compared to On-Demand instance pricing. 

### 「SPOT INSTANCE」
[Refer to: Amazon EC2 Spot Instances Pricing](https://aws.amazon.com/ec2/spot/pricing/)

The _Spot instance_ is the `spare resources` of AWS computers, that being said, its existence **uncertain**, it all depends on the market.

The price for a _Spot instance_ is always changing. And the way to use it is to set a **maximum hourly price** for each instance. When the price hit the limitation you've set, the instance will be automatically **TERMINATED**!

> Hence, it's not good for long term running, but rather for short term computation needs.

For Asia Pacific (Singapore):
- General purposes:
![image](https://user-images.githubusercontent.com/14041622/45222405-12f47400-b2e7-11e8-8baa-2a1a8f563271.png)
- Compute Optimized:
- GPU Instances:
![image](https://user-images.githubusercontent.com/14041622/45222449-31f30600-b2e7-11e8-8fa8-8aab2afad3c3.png)
- Memory Optimized:
- Storage Optimized:
- Micro Instances:
![image](https://user-images.githubusercontent.com/14041622/45222497-5a7b0000-b2e7-11e8-9d0b-451e3b1807e1.png)

> * Cluster GPU Instances are not available in all regions.



### 「ON-DEMAND」 Instance  (Standard)

[Refer to: Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/on-demand/)

For Asia Pacific (Singapore):
- General purposes:
![image](https://user-images.githubusercontent.com/14041622/45221740-f35c4c00-b2e4-11e8-91ca-35c38ecbdea9.png)
- Compute Optimized:
![image](https://user-images.githubusercontent.com/14041622/45221899-7c738300-b2e5-11e8-8927-620a04879f7c.png)
- GPU Instances:
![image](https://user-images.githubusercontent.com/14041622/45221948-a0cf5f80-b2e5-11e8-8dbd-7819864889fc.png)
- Memory Optimized:
![image](https://user-images.githubusercontent.com/14041622/45221968-afb61200-b2e5-11e8-9525-cfd322ffc5e0.png)
- Storage Optimized:
![image](https://user-images.githubusercontent.com/14041622/45221972-b6448980-b2e5-11e8-9e51-6c3f56adf33e.png)

Data transfer:
- All data Transfer IN: **FREE**
- Data Transfer OUT:
![image](https://user-images.githubusercontent.com/14041622/45222629-a037c880-b2e7-11e8-95d9-06c9deaf2e8c.png)


### 「RESERVED」 Instance (Yearly contract)
[Refer to: Amazon EC2 Reserved Instances Pricing](https://aws.amazon.com/ec2/pricing/reserved-instances/pricing/)


### 「DETICATED HOST」Instance
[Refer to: Amazon EC2 Dedicated Hosts Pricing](https://aws.amazon.com/ec2/dedicated-hosts/pricing/)


### 「EBS」Elastic Block Storage (including AMI)

[Refer to: Amazon EBS Pricing](https://aws.amazon.com/ebs/pricing/)
[Refer to Stackoverflow: Cost of storing AMI](https://stackoverflow.com/questions/18650697/cost-of-storing-ami)

