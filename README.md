# engineers-musings-code

Companion code and Colab notebooks for the **[An Engineer's musings](https://engineers-musings.pages.dev)** blog.

The blog itself lives in a separate (private) repo; this public repo holds the
runnable artifacts so the "Open in Colab" buttons in the posts resolve for
everyone. Colab loads notebooks straight from GitHub, which requires the host
repo to be public.

## Layout

```
notebooks/<series>/<phase>/<NN-slug>.ipynb
```

For example, the *Practical PyTorch* series:

```
notebooks/pytorch/phase-1/01-what-is-pytorch.ipynb
```

Each notebook is the companion to the post of the same slug. Open one in Colab:

```
https://colab.research.google.com/github/engineers-musings/engineers-musings-code/blob/main/<path-to>.ipynb
```
