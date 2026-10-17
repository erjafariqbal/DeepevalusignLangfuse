from typing import Optional, List, Dict, Any
from langfuse_config import langfuse


def log_test_execution(

           *,
                framework: str,
                test_name:str,
                score: float,
                status: str,
        
                input: Optional[str] = None,
                actual_output: Optional[str] = None,
                context: Optional[List[str]] = None,
                expected_output: Optional[str] = None,
                retrieval_context: Optional[List[str]] = None,
                model: Optional[str] = "gpt-4o-mini",
                latency: Optional[str] = None,
                token: Optional[str] = None,
                metadata: Optional[Dict[str, Any]] = None
        
):
    with langfuse.start_as_current_observation(

        name= test_name,
        as_type= "generation",
        model = model,
        metadata={
            "framework": framework,
            "status": status,
            "expected_output": expected_output,
            "context": context,
            "retrieval_context": retrieval_context,
            "latency_ms": latency,
            "token": token,
            **(metadata or {})
        }


    ) as generation:

        generation.update(
            input=input,
            output=actual_output

        )

        langfuse.score_current_trace(
            name = test_name,
            value= float(score),
            comment= status

        )

        langfuse.flush()


     



    


       

        

