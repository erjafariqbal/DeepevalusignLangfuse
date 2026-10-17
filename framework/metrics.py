
from deepeval.metrics import GEval
from framework.config import THRESHOLDS
from framework.metrics_config import METRIC_CONFIG


# Create a generic metric builder

def build_metric(name, criteria, evaluation_param, evaluation_steps, threshold):
    return GEval(
        name=name,
        criteria=criteria,
        evaluation_params=evaluation_param,
        evaluation_steps=evaluation_steps,
        threshold=threshold,
    )


def get_metric(metric_name):
    config = METRIC_CONFIG[metric_name]

    return build_metric(
        name=metric_name,
        criteria=config["criteria"],
        evaluation_param=config["evaluation_params"],
        evaluation_steps=config["evaluation_steps"],
        threshold=THRESHOLDS.get(metric_name, 0.8),
    )
