"""
this code create a Bell's state (|00> + |11>)
and measure it 1000 times
"""

from qiskit import QuantumProgram
qp = QuantumProgram()
qr = qp.create_quantum_register('qr',2)
cr = qp.create_classical_register('cr',2)
qc = qp.create_circuit('Bell',[qr],[cr])
qc.h(qr[0])  #apply hadamar gate
qc.cx(qr[0], qr[1]) #apply cx gate
qc.measure(qr[0], cr[0])
qc.measure(qr[1], cr[1])
result = qp.execute('Bell')
print(result.get_counts('Bell'))


#https://www.softynews.com/optional-tutorial-qiskit-quantum-computing-platform/