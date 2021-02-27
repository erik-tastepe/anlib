# anlib

## What is it?

A command-line application for querying and downloading books/articles from the [Anarchist Library](theanarchistlibrary.org).

## How do I download it?

Easy.

```shell
pip install anlib
```

## Cool, so how do I use i...

Easy.

```shell
anlib <search-term> # anlib syndicalism
```

The reading material launches by default in your default browser. If you would instead like to download the material at the current location in your terminal, pass the `-m` flag.

```shell
anlib <search-term> -m download
```

Additionally, it launches or downloads a `.html` file by default; if you would instead like to use a `.pdf`, pass the `-e` flag.

```shell
anlib <search-term> -e .pdf
```

## Future Work

The application is very much still in the beta phase. If you have any suggestions or run into any issues, please feel free to open an issue or contact me!
