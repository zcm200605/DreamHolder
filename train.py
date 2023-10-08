!pip install paddlehub==1.7 -i https://pypi.tuna.tsinghua.edu.cn/simple
!pip install --upgrade pyahocorasick -i https://pypi.tuna.tsinghua.edu.cn/simple

import paddlehub as hub
!hub install senta_lstm==1.0.0
module=hub.Module(name="senta_lstm")
dataset = hub.dataset.ChnSentiCorp()

reader=hub.reader.LACClassifyReader(
    dataset=dataset, vocab_path=module.get_vocab_path())

strategy = hub.AdamWeightDecayStrategy(
    weight_decay=0.01,
    lr_scheduler="linear_decay",
    warmup_proportion=0.1,
    learning_rate=5e-5)

config=hub.RunConfig(
    use_data_parallel=True,
    num_epoch=7500,
    use_cuda=True,
    checkpoint_dir="nlp_senta_turtorial_demo",
    batch_size=128,
    log_interval=10,
    eval_interval=50,
    strategy=strategy)


inputs,outputs,program=module.context(trainable=True)
#words = inputs["text"]
sent_feature=outputs["sentence_feature"]
feed_list=[inputs["words"].name]
cls_task=hub.TextClassifierTask(
    data_reader=reader,
    feature=sent_feature,
    feed_list=feed_list,
    num_classes=dataset.num_labels,
    config=config)


run_states=cls_task.finetune_and_eval()

import numpy as np
import copy
predicted_data=["这家餐厅很好吃", "这部电影真的很差劲"]
data = copy.deepcopy(predicted_data)
run_states=cls_task.predict(data=data)
results=[run_state.run_results for run_state in run_states]
index=0
for batch_result in results:
    batch_result = np.argmax(batch_result, axis=2)[0]
    for result in batch_result:
        print("%s\tpredict=%s" % (predicted_data[index], result))
        index += 1 






