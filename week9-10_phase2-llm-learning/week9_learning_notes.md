Week 9-10: LLM Fundamentals - My Learning Notes
Sources used:

Article: "The Illustrated Transformer" by Jay Alammar (jalammar.github.io/illustrated-transformer)
Video: "But what is a Neural Network? | Deep Learning, Chapter 1" by 3Blue1Brown (Grant Sanderson)


1. What is a Transformer?

A transformer is a neural network architecture made of two main parts: an encoder stack and a decoder stack, originally built for tasks like machine translation. Instead of processing words one at a time in order (like older RNN-based models did), it uses a mechanism called self-attention to let every word "look at" every other word in the sentence at once. This makes transformers much faster to train because the calculations can be parallelized, and it's the architecture behind basically every modern large language model, including Claude.

2. How Does Attention Mechanism Work?

Self-attention works by turning each word into three vectors — a Query, a Key, and a Value — using weight matrices the model learns during training. To figure out how much a word should "pay attention" to other words, the model takes the dot product of its Query vector with every other word's Key vector, scales and runs the result through softmax to get a set of weights that add up to 1, and then uses those weights to blend together the Value vectors. So in the classic example sentence "The animal didn't cross the street because it was too tired," attention is what lets the model figure out that "it" refers to "the animal" rather than "the street." The Transformer also uses multiple attention "heads" running in parallel, so the model can focus on different kinds of relationships between words at the same time, not just one.

3. What are Tokens?

Tokens are the basic units of text a model actually processes — sometimes a whole word, sometimes a piece of a word, sometimes punctuation. Before any attention or computation happens, each token gets converted into a vector (an embedding), and a positional encoding vector is added on top so the model also knows the order the tokens appeared in (since attention by itself has no built-in sense of sequence). Tokens matter practically too, since API pricing and context limits are measured in tokens, not words or characters.

4. What is a Context Window?

A context window is the maximum number of tokens a model can take in and "see" at once when generating a response — it includes the conversation history, any documents pasted in, and the response itself. Because a transformer's attention mechanism compares every token to every other token, everything inside the context window is processed together in a single pass rather than being remembered step-by-step like older models. A larger context window means a model can hold onto much more text — a long document or a long conversation — without losing earlier details.

5. Why is Temperature Important?

After the decoder produces a probability distribution over the vocabulary (via the final linear + softmax layer described in the article), the model has to pick which word to output next. Temperature controls how that choice is made: a low temperature sharpens the distribution so the model almost always picks the highest-probability word, giving consistent, predictable output, while a higher temperature flattens the distribution so lower-probability words get picked more often, giving more varied and creative output. So you'd choose a low temperature for factual or deterministic tasks and a higher one for brainstorming or creative writing.

6. Key Insight: Why This Matters for Me

The biggest surprise was realizing the transformer has no memory or hidden state carried over time the way RNNs do — it processes the entire input sequence at once, and "context" only exists because every token can attend to every other token within the same pass. The 3Blue1Brown video reinforced this from the basic neural-network side: a network is fundamentally just layers of neurons holding numbers, connected by weights and biases, with no built-in concept of sequence or memory — the Transformer's positional encoding and attention are specifically bolted on to make that work for language. That explains why the context window is such a big deal: if something isn't inside it, the model genuinely cannot "see" it, there's no memory to fall back on.

7. Ready for APIs?

I want to build a small tool that uses the Claude API to answer questions grounded in my own documents, and experiment with adjusting temperature and context to see how it changes the output in practice — basically connecting the theory from this week to something hands-on.