import streamlit as st
import pandas as pd
import numpy as np
import presidio_analyzer
import presidio_anonymizer
import spacy
import spacy_streamlit
import time


from presidio_anonymizer import AnonymizerEngine, DeanonymizeEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorResult, OperatorConfig
from presidio_anonymizer.operators import Decrypt

crypto_key = "WmZq4t7w!z%C&F)J"

engine = AnonymizerEngine()

# Invoke the anonymize function with the text,
# analyzer results (potentially coming from presidio-analyzer)
# and an 'encrypt' operator to get an encrypted anonymization output:
start_time = time.time()

person_name = "John Smith"

anonymize_result = engine.anonymize(
    text=person_name,
    analyzer_results=[
        RecognizerResult(entity_type="PERSON", start=0, end=len(person_name), score=0.8),
    ],
    operators={"PERSON": OperatorConfig("encrypt", {"key": crypto_key})},
)

anonymize_result
end_time = time.time()
execution_time = (end_time - start_time) * 1000  # Convert to milliseconds

execution_time

start_time = time.time()

encrypted_entity_value = anonymize_result.items[0].text

encryypted_passed_value = "NYPbQLfbHxBxiwHl5rO/Lv9xbrkPvjuIfopElvr0zLs="

# Restore the original entity value
decrypted = Decrypt().operate(text=encryypted_passed_value, params={"key": crypto_key})
decrypted
end_time = time.time()
execution_time = (end_time - start_time) * 1000  # Convert to milliseconds

execution_time