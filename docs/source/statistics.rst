.. _statistics:

VerticaPy Statistics Page
=========================

Welcome to the VerticaPy Statistics Page! This page provides a comprehensive overview of the statistics generated by VerticaPy for your data. VerticaPy offers a set of functions to compute these statistics for each new version of your project, allowing you to stay informed about the characteristics and trends in your data.

Summary
-------

.. ipython:: python
   :suppress:

   import verticapy as vp
   from verticapy._utils._inspect_statistics import summarise_verticapy_chart
   vp.set_option("plotting_lib", "highcharts")
   fig = summarise_verticapy_chart()
   html_text = fig.htmlcontent.replace("container", "plotting_highcharts_barh_1D")
   with open("/project/data/VerticaPy/docs/figures/plotting_summarise_verticapy_chart.html", "w") as file:
      file.write(html_text)

Here is a drill-down bar chart summarizing the VerticaPy statistics. Each bar represents a key statistic, and you can click on each bar to explore further details. Whether you're interested in total records, mean age, maximum salary, minimum salary, or total transactions, this chart provides a quick snapshot of your data.

.. raw:: html
  :file: /project/data/VerticaPy/docs/figures/plotting_summarise_verticapy_chart.html

Table: VerticaPy Statistics Summary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. ipython:: python
  :suppress:

  # Import the function.
  from verticapy._utils._inspect_statistics import gen_rst_summary_table

  # Example.
  print(gen_rst_summary_table())
  file_path = "statistics.rst"
  with open(file_path, "w") as rst_file:
    rst_file.write(gen_rst_summary_table())

.. include:: ../statistics.rst

Code Coverage
-------------

.. ipython:: python
   :suppress:

   from verticapy._utils._inspect_statistics import codecov_verticapy_chart
   vp.set_option("plotting_lib", "plotly")
   fig = codecov_verticapy_chart()
   fig.write_html("/project/data/VerticaPy/docs/figures/plotting_codecov_verticapy_chart.html")

Here is a pie chart illustrating the code coverage for your VerticaPy project. This chart provides insights into the comprehensiveness of your codebase and areas that may require additional attention.

.. raw:: html
  :file: /project/data/VerticaPy/docs/figures/plotting_codecov_verticapy_chart.html

Exploration and Discovery
--------------------------

VerticaPy empowers you to explore and discover interesting findings within your data. Whether you're tracking changes over versions or uncovering patterns in code coverage, there's always something new to learn. Be sure to use VerticaPy's functions and tools to compute statistics for each new version and dive into the details to make informed decisions for your project.

Details and Code
----------------

For more details and to generate these charts and tables, refer to the following Python code:

.. code-block:: python
   
   # Imports
   from verticapy._utils._inspect_statistics import codecov_verticapy_chart, gen_rst_summary_table, summarise_verticapy_chart

   # Generates the VerticaPy Drilldown Chart
   summarise_verticapy_chart()

   # Generates the VerticaPy Codecov Chart
   codecov_verticapy_chart()

   # Generates the VerticaPy RST Table
   gen_rst_summary_table()


.. seealso::

  `Code Coverage <https://app.codecov.io/gh/vertica/VerticaPy>`_