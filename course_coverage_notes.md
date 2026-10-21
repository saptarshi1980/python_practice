# Bridge from the existing course

The current README and all 21 current notebooks were inspected before creating Lessons 22–27.
Current notebooks, rather than recovery copies, informed the sequence. Existing notebooks are
unchanged. Their practice format is retained: numbered explanations, small commented examples,
known-result checks, blank practice scaffolds, a chapter project, and reflection.

| Existing coverage | Where | Treatment in the new sequence |
| --- | --- | --- |
| Ordered sequences, indexing, slicing, membership, mutation, shallow copying | 3–4 | Applied to array shapes, masks, and views in 22 |
| Key membership, get, keys/values/items, list of employee dictionaries | 6 | Applied to labeled tables and joins in 23 |
| Set uniqueness, membership, operations, unordered display | 6 | Used for schema/citation checks in 27 |
| List/tuple conversion, dictionary view-to-list conversion, dictionary/set comprehensions | 4, 6, 9 | Applied to tabular and JSON boundaries, not repeated as a general collection lesson |
| enumerate, zip(strict=True), starred and dictionary unpacking | 9 | Used in data preparation and chunk provenance |
| Functions, keyword-only parameters, defaults, scope, mutable-default pitfalls | 7 | Reused for transformation, training, inference, and client boundaries |
| OOP, validated properties, inheritance, abstraction, composition, class/static methods | 13 | Applied to Dataset, inference services, and mock clients |
| Iterators, generators, laziness, bounded consumption | 14 | Bridge to batching and chunking |
| Callable keys, lambda, tuple sort keys, any/all, partial | 15 | Used in ranking and validation |
| Dataclasses, collection/optional hints, post-init validation, serialization | 16 | Bridge to Pydantic runtime contracts in 26 |
| Exceptions, finite checks, per-record rejection | 8, 20 | Applied at numerical, HTTP, and AI boundaries |
| pathlib, temporary files, CSV/JSON; modules, imports, main guard | 10–11 | Reused for artifacts and API module layout |
| Decimal/date policies | 12, 20 | Retained for accounting; new numerical examples use energy measurements |
| unittest, known-answer/boundary tests, logging, debugging | 17 | Applied through assertions, service doubles, endpoint tests, and evaluations |
| Counter/defaultdict, regex, custom context manager | 18 | Used where practical without another foundations chapter |
| SQLite, transactions, parameterized SQL, MySQL, joins, repository design | 19–21 | Bridge to pandas joins; no live database requirement in new lessons |

Some foundations are brief or absent: explicit list.index searching, arbitrary dictionary-to-record
conversion recipes, map/filter, variadic function parameters, and custom decorator implementation
are not comprehensive topics in the existing sequence. They are not prerequisites for these six
lessons. New operations are explained when first used (notably decorators for route registration,
array broadcasting, Pipeline state, autograd, runtime schemas, async waiting, and vector retrieval).

The six new lessons introduce the third-party data/AI stack rather than recasting the existing
payroll chapters. All data is fictional; no server, credentials, external model, or network is
needed for core learning examples. Lesson 27's lexical vectors and deterministic client are
explicit teaching substitutes, not claims of semantic embeddings or real LLM evaluation.


## Added at learner request: Lesson 6A

06_A_modern_function.ipynb is an explicit bridge/review after the original Lesson 6. It fills
collection search and conversion gaps, introduces function tools and typed records, and links
back to the existing later chapters for depth. Its companion answer key has ten explained
exercise solutions and a tested directory-report project. All dependencies are now consolidated
in requirements.txt; existing dependency entries were retained and separate stage files removed.


## Added visualization bridge: Lesson 23A

23_A_data_visualization.ipynb follows pandas and precedes classical ML without renumbering
existing lessons. It adds Matplotlib, Seaborn, and Plotly, including chart selection, units,
distributions, group comparisons, correlation limitations, interactive exploration, and offline
exports. It uses the public bundled scikit-learn Iris dataset rather than fictional records,
as explicitly allowed for this chapter. Six exercises and a report project have a separate
explained answer key. All dependencies remain in the one requirements.txt.
