
import allure
from deepeval.test_case import LLMTestCase
from deepeval.evaluate import evaluate
from typing import Optional
from langfuse_logger import log_test_execution


def bulit_llm_test_case(
        chatbot_fun: callable,
        prompt: str,
        context: Optional[str] = None,
        expected_output: Optional[str] = None,
        retrieval_context: Optional[list[str]] = None,
        tittle: Optional[str] = None
        ):

    response = chatbot_fun(prompt)

    if tittle:
        allure.dynamic.title(tittle)

    allure.attach(
        prompt,
        name="Query",
        attachment_type=allure.attachment_type.TEXT
    )
    allure.attach(
        response,
        name="Response",
        attachment_type=allure.attachment_type.TEXT
    )

    if context:
        allure.attach(
            str(context),
            name="Context",
            attachment_type=allure.attachment_type.TEXT
        )

    if expected_output:
        allure.attach(
            str(expected_output),
            name="Expected Output",
            attachment_type=allure.attachment_type.TEXT
        )

    if retrieval_context:
        allure.attach(
            str(retrieval_context),
            name="Rereieval Context",
            attachment_type=allure.attachment_type.TEXT
        )

    return LLMTestCase(
        input=prompt,
        actual_output=response,
        expected_output=expected_output,
        context=context,
        retrieval_context=retrieval_context
    )


def evaluate_and_log(test_case, metric, test_name):
    results = evaluate([test_case], [metric])

    test_result = results.test_results[0]

    metric_result = next(
        item for item in test_result.metrics
        if item.name == metric.__name__
    )

    score = metric_result.score
    status = "PASSED" if metric_result.success else "FAILED"

    if score is None:
        raise ValueError(
            f"DeepEval returned no score for {test_name}"
        )

    log_test_execution(
        framework="DeepEval",
        test_name=test_name,
        score=float(score),
        status=status,
        input=test_case.input,
        actual_output=test_case.actual_output,
        expected_output=test_case.expected_output,
        context=test_case.context,
        retrieval_context=test_case.retrieval_context,
    )

    return results


# import allure
# from deepeval.test_case import LLMTestCase
# from typing import List, Optional, Dict, Callable
# def bulit_llm_test_case(
#         chatbot_fun: callable,
#         prompt: str,
#         context: Optional[str] = None,
#         expected_output: Optional[str] = None,
#         retrieval_context: Optional[list[str]] = None,

#         tittle: Optional[str] = None
#         ):

    
#     response = chatbot_fun(prompt)   #chatbot Prompt

#     if tittle:
#         allure.dynamic.title(tittle)
    
#     allure.attach(prompt, name= "Query", attachment_type= allure.attachment_type.TEXT)
#     allure.attach(response, name= "Response", attachment_type= allure.attachment_type.TEXT)

#     if context:
#         allure.attach(str(context) , name= "Context", attachment_type= allure.attachment_type.TEXT)

#     if expected_output:
#         allure.attach(str(expected_output) , name= "Expected Output", attachment_type= allure.attachment_type.TEXT)

#     if retrieval_context:
#         allure.attach(str(retrieval_context) , name= "Rereieval Context", attachment_type= allure.attachment_type.TEXT)
        
    



#     return LLMTestCase(
#         input= prompt,
#         actual_output= response,
#         expected_output= expected_output,
#         context=context,
#         retrieval_context= retrieval_context
#     )