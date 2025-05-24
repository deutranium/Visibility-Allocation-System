# Visibility Allocation Systems (VAS)

The library allows anyone to define a VAS pipeline, along with components like tools, metrics, and dataflow (i.e. how components are connected). This library serves as a unifying interface and gives a base structure for anyone who would like to define their own tools/metrics/pipeline.

## How to use this library
`VAS` outlines a structure that other VAS components like pipeline, tools etc. should follow. Eg. if you want to create a pipeline, you should create a pipeline class that is a child of `VAS.pipeline.Pipeline` and satisfies all the conditions of the parent class. Similarly, you can define tools and metrics as subclasses of `VAS.tools.Tool` and `VAS.metrics.Metric` respectively. The VAS classes already contain certain rules, eg. a metric should return a `pandas.Series` object and should have the same number of rows as the dataset, etc. These are done to ensure that the same VAS pipeline can be used across disciplines and tools.

## Components
On an implementaion level, VAS can broadly be categorized into three main components:

### Pipeline
Defines the dataflow and connections between different tools.

A pipeline should inherit from `VAS.pipeline.Pipeline`, and should have the following methods:
1. `_add_tool()`: Adding a tool
2. `_add_connection()`: Adding a connection between tools
3. `_add_metric()`: Adding a metric along with information about what tools to evaluate
4. `_run()`: How to run a pipeline. This could be a simple breadth first search starting from the first tool, or any other variation.
5. `_evaluate_metrics()`: How to evaluate metrics

### Tools
The building blocks of a VAS pipeline, tools can be thought of as functions that are applied to the said dataset. We introduce three subclasses of `VAS.tools.Tool` - `VAS.tools.Sort`, `VAS.tools.Search` and `VAS.tools.Filter` to define sort, search and filter tools respectively. If you want to create any custom tools, please create a subclass of `VAS.tools.Tool` to implement it.

### Metrics
We use metrics to focus on evaluation part of a VAS ecosystem. A metric can be created as a subclass of `VAS.metrics.Metric` and can be _attached_ to multiple tools.

#### vas_addons
We have implemented a pipeline, few tools and metrics to give a headstart to someone who wants to create a basic pipeline with the said tools. These implementations also serve as an example for structure for anyone who would like to implement their own components.