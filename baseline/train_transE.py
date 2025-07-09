from pykeen.datasets import get_dataset
from pykeen.pipeline import pipeline

# Load the FB15k-237 dataset (automatically downloads)
dataset = get_dataset(dataset='FB15k237')

# Run a simple pipeline with TransE
result = pipeline(
    dataset=dataset,
    model='TransE',
    training_loop='sLCWA',
    epochs=10,  # small number for prototype
    random_seed=42,
    training_kwargs=dict(num_workers=2),
)

# Print evaluation metrics
metrics = result.get_metric_results()
print(metrics.to_dict())
