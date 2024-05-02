<img src="./img/infineon_logo.png" alt="Infineon Logo" height="50"/>

# Improving Customer Experience with Generative AI

:information_source: **Please check [here](./submission) for details about the project submission.**

## Running the Example

### Preparation

Please start by installing [Python](https://www.python.org/) and [Pip](https://pypi.org/project/pip/).

Now you can install the required Python package for working with LLAMA2:
```
pip install llama-cpp-python
```

If you don't have Pandas installed you will also have to install it:
```
pip install pandas
```

Afterwards you can clone this git repo:
```
git clone https://github.com/Infineon/hackathon
cd hackathon
cd examples
```

### Run the example

You can run the LLMA example with this command:
```
python llama_example.py
```

### Output
The example takes a random GitHub issue from Infineon's GitHub org and outputs something like:
```
...
------------------------------
Selected issue:
Subject: Question: How to use examples with a particular kit
Request: Trying to use these examples with the Prototyping Kit BT WiFi

Is there some manual configuration that needs to be done on my end or is there a setting that will select the target board?
------------------------------

...
Model output:

Urgency level: 3 (somewhat urgent)
...
```

Of course this is only an example to get one potential workflow running and can still output complete trash - doing it better is your task :)

## Hackathon Material
* [Challenge Introduction Slides](./challenge_introduction.pdf)
* [GitHub issues in Pickle format](./examples/github_issues.pkl)

## Useful Links
* [Infineon Developer Community](https://community.infineon.com/)

## Infineon Team

**Eric** (Embedded Systems Engineer)

<img src="./img/eric.png" alt="Eric" height="150"/>

**Julian** (Staff Embedded Systems Engineer)

<img src="./img/julian.png" alt="Julian" height="150"/>

### How to reach us?
Please [open an issue](https://github.com/Infineon/hackathon/issues) in this repository to ask your questions or talk to us at the location :)