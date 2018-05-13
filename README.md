# Quantum Computing

<img align="right" src="https://raw.githubusercontent.com/Aurelien-Pelissier/IBMQ-Quantum-Computing/master/img/Complexity.jpg" width=450>
During the past decade, considerable progress has been achieved regarding the development of quantum computers, and a breakthrough in this field will have massive application particularily in research, cryptography and logistic. Google and IBM recently claimed the creation of a 72 and 50 qubit quantum chips respectively, making the possibility for a potential imminent quantum supremacy even more likely.  


&nbsp;

In May 2016, IBM launched Quantum Experience (QX), which enables anyone to easily connect to its 5qubit quantum processors via the IBM Cloud. (https://www.research.ibm.com/ibm-q/). Along with it's platform, IBM also developped `QISKit`, a Python library for the Quantum Experience API, where users can more easily apply quantum gates to run complex quantum algorithms and experiments.  

This repository is an introdution to quantum computing and contain the source code to run simples quantum algorithms. They are implemented with the python library `QISKit`, that can be easily installed with the command `$ pip install qiskit` (`Python 3.5` is required). More information is available at https://qiskit.org/.

## Quantum Gates

<img align="left" src="https://raw.githubusercontent.com/Aurelien-Pelissier/IBMQ-Quantum-Computing/master/img/gate.png" width=170>
In analogy with the classical gates NOT, AND, OR, ... that are the building blocks for classical circuits, there are quantum gates that perform basic operations on qubits. The most common quantum gates are summarized here --> https://en.wikipedia.org/wiki/Quantum_logic_gate. 

For example, the Hadamard gate, H, perform the following operartion:
<img align="left" src="https://raw.githubusercontent.com/Aurelien-Pelissier/IBMQ-Quantum-Computing/master/img/hadamar.png" width=550>



&nbsp;

&nbsp;


### Creating and measuring a Bell state
The following code create a Bell state and measure it 1000 times. 

<img src="https://raw.githubusercontent.com/Aurelien-Pelissier/IBMQ-Quantum-Computing/master/img/Bell.png" width=180>

```python
from qiskit import QuantumProgram
qp = QuantumProgram()
qr = qp.create_quantum_register('qr',2)      #Initialize 2 qubits to perform operations
cr = qp.create_classical_register('qc',2)    #Initialize 2 classical bits to store the measurements
qc = qp.create_circuit('Bell',[qr],[cr])
qc.h(qr[0])                                  #Apply Hadamar gate
qc.cx(qr[0], qr[1])                          #Apply CNOT gate
qc.measure(qr[0], cr[0])                     #Measure qubit 0 and store the result in bit 0
qc.measure(qr[1], cr[1])                     #Measure qubit 1 and store the result in bit 1

result = qp.execute('Bell', shots=1000)      #Compile and run the Quantum Program 1000 times
print(result.get_counts('Bell'))
```
a possible result that we get is
```python
{'11': 494, '00': 506}
```




&nbsp;


## Shor's algorithm
