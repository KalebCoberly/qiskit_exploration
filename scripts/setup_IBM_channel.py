"""Set up the IBM Quantum Platform channel for Qiskit Runtime Service.

Follows along to https://docs.quantum.ibm.com/guides/setup-channel
"""

import os

from dotenv import load_dotenv
import logging

from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    QiskitRuntimeService.save_account(
        token=get_ibm_quantum_token(),
        instance=get_CRN_instance(),
        # channel="ibm_quantum",  # IBM Quantum Platform channel (vs. IBM Cloud platform).
        name="Functions_test-open_plan",
        set_as_default=True,
        overwrite=True,
    )
    print("IBM Quantum Platform channel set up successfully. Testing service ...")
    test_service()

    return

def get_key(name: str) -> str:
    """Get specified key from dotenv file."""
    load_dotenv()
    key = os.getenv(name)
    if not key:
        raise ValueError(
            f"{name} not found. Set the environment variable."
        )

    return key


def get_ibm_quantum_token() -> str:
    """Get the IBM Quantum API token."""
    return get_key("IBM_QUANTUM_API_TOKEN")


def get_CRN_instance() -> str:
    """Get the IBM Cloud CRN instance."""
    return get_key("IBM_CLOUD_CRN_INSTANCE")


def test_service() -> None:
    """Test the Qiskit Runtime Service."""
    # Spent 2 hours and 40 minutes in queue.
    # Estimated quantum runtime: 3.4s.
    # Actual: 9s.
    example_circuit = QuantumCircuit(2)
    example_circuit.measure_all()
    
    # Now that the account is saved, we can use the Qiskit Runtime without specifying further authentication.
    service = QiskitRuntimeService()
    backend = service.least_busy(operational=True, simulator=False)
    
    sampler = Sampler(backend)

    logger.info("Running the circuit on the backend ...")
    job = sampler.run([example_circuit])
    logger.info(f"job id: {job.job_id()}")

    logger.info("Getting the result ...")
    result = job.result()
    logger.info(result)

    return
 

if __name__ == "__main__":
    main()