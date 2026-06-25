# blog-companion

Companion code and Colab notebooks for the **[An Engineer's musings](https://engineers-musings.pages.dev)** blog.

The blog itself lives in a separate (private) repo; this public repo holds the
runnable artifacts so the "Open in Colab" buttons in the posts resolve for
everyone. Colab loads notebooks straight from GitHub, which requires the host
repo to be public.

## Layout

One folder per series, with notebooks named to match the post slug:

```
<series>/<NN-slug>.ipynb
```

For example, the *Running Models — Foundations* series:

```
running-models-foundations/01-what-is-pytorch.ipynb
```

Open one in Colab:

```
https://colab.research.google.com/github/engineers-musings/blog-companion/blob/main/<path>.ipynb
```
