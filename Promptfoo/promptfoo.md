# Types of testing using promptfoo

## Deterministic Testing

We can use promptfoo for deterministic testing:

In this case we will create a test case with specific input and expected output.

```yaml
assert:
    type:
    value:
```

1. **contains** - To check if the output contains a specific word or phrase.
2. **equals** - To check if the output is exactly equal to the expected output.
3. **regex** - To check if the output matches a specific regular expression pattern.
4. **not-contains** - To check if the output not contains a specific word or phrase.
5. **starts-with** - To check if the output starts with a specific word or phrase.
6. **ends-with** - To check if the output ends with a specific word or phrase
7. **is-json** - To check if the output is a valid json string
8. **javascript** - To execute a custom javascript function to validate the output:
   ex: 2+2 = 4 - `output.includes("4")`
9. **contains-any** - To check if the output contains any of the specific word or phrase.
10. **contains-all** - To check if the output contains all of the specific word or phrase.
11. **icontains** - To check if the output contains a specific word or phrase, ignoring the case.

FIXED DEPOSITE - fixed deposite

---

## Non-Deterministic Testing

We can also use promptfoo for non-deterministic testing of llms.

In this case we create a test case with speific inputs without the expected outputs.

We can use promptfoo t evaluate the evaluation of LLM and analyze the result.

1. **LLM as a judge**
   - llm-rubric
   - Red Teaming
   - MITRE ATLAS
   - NIST AI

---

## Model Graded

1. **answer-relevance**
2. **factuality**
3. **context-relevance**
4. **context-recall**
5. **context-faithfulness**
6. **g-eval**

---

## Providers

**By using model id** - gpt-40-mini, id:xyz-1o

**By Using API** -

```yaml
id - http
config:
    url : http://127.0.0.1:8000
    method : GET/POST/PUT/DELETE - POST
    body:
        query
```

API - `http://127.0.0.1:8000/chat`

---

## Config File Structure

```yaml
description: What is the test about
providers:
    - id : model that you are testing

prompts:
    - "prompt"

tests:
    - vars:
        query: ""
      assert:
        - type: contains
          value: "fixed tenure"
        - type: icontains
          value: "Fixed Tenure"
    - vars:
        query: ""
    assert:
        - type: contains
          value: "fixed tenure"
        - type: icontains
          value: "Fixed Tenure"
```

---

## Run Command

```bash
# promptfoo eval -c pathOfTheYamlFile
```