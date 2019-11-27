python -m scripts.retrain \
bottleneck_dir=tf_files/bottlenecks \
how_many_training_steps=500 \
model_dir=tf_files/models/ \
summaries_dir=tf_files/training_summaries/"mobilenet" \
output_graph=tf_files/retrained_graph.pb \
output_labels=tf_files/retrained_labels.txt \
architecture="mobilenet_1.0_224" \
image_dir=E:\PlantVillage-Dataset-master\raw\color