# qiskit_exploration

Quantum computing hello worlds, notebooks, etc. Follows along to IBM Qiskit guides: https://docs.quantum.ibm.com/guides

## Setting up

1. Install the required dependencies:

```
$ pip install requirements.txt
```

2. Create an IBM Quantum account at quantum.ibm.com, and paste your API token in a ``.env`` file as ``IBM_QUANTUM_API_TOKEN``.

3. Save your IBM Quantum Platform account by running ``scripts/setup_IBM_channel.py``. (If you would rather set up an IBM Cloud account, see https://docs.quantum.ibm.com/guides/setup-channel)