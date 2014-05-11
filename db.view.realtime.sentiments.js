{
  "_id": "_design/realtime",
  "_rev": "1-500c2bc46f1d96d4603d4d7b52b1cee1",
  "views": {
    "sentiments": {
      "reduce": "_sum",
      "map": "function(doc) {\n  var sentiments = {};\n  sentiments[doc.sentiment] = 1;\n  emit(doc.datetime, sentiments);\n}"
    }
  },
  "language": "javascript"
}
