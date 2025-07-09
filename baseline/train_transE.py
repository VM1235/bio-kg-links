from pykeen.datasets import get_dataset
from pykeen.pipeline import pipeline

def run():
    dataset = get_dataset(dataset='FB15k237')

    result = pipeline(
        dataset=dataset,
        model='TransE',
        training_loop='sLCWA',
        epochs=10,
        random_seed=42,
        training_kwargs=dict(num_workers=0),  # Safe on macOS
    )

    metrics = result.metric_results.to_dict()

    print("\nEvaluation Metrics:")
    for k, v in metrics.items():
        if isinstance(v, (float, int)):
            print(f"{k}: {v:.4f}")
        else:
            print(f"{k}: {v}")  # Just print the dict or list as-is

    with open("baseline/transE_metrics.txt", "w") as f:
        for k, v in metrics.items():
            if isinstance(v, (float, int)):
                f.write(f"{k}: {v:.4f}\n")
            else:
                f.write(f"{k}: {v}\n")

if __name__ == "__main__":
    run()
