from flask import Blueprint, request, jsonify, abort
from config import ins_config
from lib.zero_shot import ZeroShot

model_id = ins_config.getDefault("model_id")
cache_dir = ins_config.getDefault("cache_dir")
json_data_path = ins_config.getDefault("json_data_path")
zero_shot_classifier = ZeroShot(model_id, json_data_path, cache_dir)

router = Blueprint("zero-shot", __name__)


@router.route("/", methods=["POST"])
def zero_shot():
    data = request.get_json()
    if "sequence" in data and "labels" in data:
        res = zero_shot_classifier.classify(data["sequence"], data["labels"])
        return jsonify(res)
    else:
        abort(400)


@router.route("/conversation", methods=["GET"])
def conversation():
    res = zero_shot_classifier.test_conversation()
    return jsonify(res)


@router.route("/sentiment-for-java", methods=["POST"])
def sentiment():
    data = request.get_json()
    labels = ["positive", "negative", "neutral"]
    if "text" in data:
        res = zero_shot_classifier.classify(data["text"], labels)
        return jsonify(res)
    else:
        abort(400)
