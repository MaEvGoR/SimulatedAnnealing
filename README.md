# Statistics Assignment 3

# How to run

```python
python3 -m virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
# open http://127.0.0.1:8050/
```

![](https://i.imgur.com/7PzMESo.png)
> Interface example

* Init - intialize algorithm
* Step - make one step of the algorithm
* Solve - make step until cooldown

# Speed of convergence

Chosen annealing rates: [0.2, 0.5, 0.8, 0.9, 0.99], with 10^5 as initial temperature. 

![](https://i.imgur.com/24wdVtN.png)

Surely, final cost depends on number of annealing rate we set. If we set rate big enough, we gonna find the solution. Problem is number of steps that requires this path to be found. 

# Grid parameters

If we take annealing rate from 0 to 0.999 with step 0.001 and starting temperature from 0 to 10^5 with step 100, we would see, that cost is not dependent on starting temperature. 

![](https://i.imgur.com/job7x7C.png)


Strong correlation is between annealing rate and final cost

![](https://i.imgur.com/kUIIxgz.png)

Density function also shows this correlation. 

![](https://i.imgur.com/H98k5Ao.png)

