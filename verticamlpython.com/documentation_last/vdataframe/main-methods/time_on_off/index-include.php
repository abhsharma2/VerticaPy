<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="vDataFrame.time_on_off">vDataFrame.time_on_off<a class="anchor-link" href="#vDataFrame.time_on_off">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">vDataFrame</span><span class="o">.</span><span class="n">time_on_off</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Displays the time took by each query.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Returns">Returns<a class="anchor-link" href="#Returns">&#182;</a></h3><p><b>vDataFrame</b> : self</p>
<h3 id="Example">Example<a class="anchor-link" href="#Example">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[52]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">vertica_ml_python.learn.datasets</span> <span class="k">import</span> <span class="n">load_titanic</span>
<span class="n">titanic</span> <span class="o">=</span> <span class="n">load_titanic</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">titanic</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>



<div class="output_html rendered_html output_subarea ">
<table style="border-collapse: collapse; border: 2px solid white"><tr ><td style="font-size:1.02em;background-color:#263133;color:white"><b></b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>fare</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>sex</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>body</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>pclass</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>age</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>name</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>cabin</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>parch</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>survived</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>boat</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>ticket</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>embarked</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>home.dest</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>sibsp</b></td></tr><tr ><td style="font-size:1.02em;background-color:#263133;color:white"><b>0</b></td><td style="border: 1px solid white;">151.55000</td><td style="border: 1px solid white;">female</td><td style="border: 1px solid white;">None</td><td style="border: 1px solid white;">1</td><td style="border: 1px solid white;">2.000</td><td style="border: 1px solid white;">Allison, Miss. Helen Loraine</td><td style="border: 1px solid white;">C22 C26</td><td style="border: 1px solid white;">2</td><td style="border: 1px solid white;">0</td><td style="border: 1px solid white;">None</td><td style="border: 1px solid white;">113781</td><td style="border: 1px solid white;">S</td><td style="border: 1px solid white;">Montreal, PQ / Chesterville, ON</td><td style="border: 1px solid white;">1</td></tr><tr ><td style="font-size:1.02em;background-color:#263133;color:white"><b>1</b></td><td style="border: 1px solid white;">151.55000</td><td style="border: 1px solid white;">male</td><td style="border: 1px solid white;">135</td><td style="border: 1px solid white;">1</td><td style="border: 1px solid white;">30.000</td><td style="border: 1px solid white;">Allison, Mr. Hudson Joshua Creighton</td><td style="border: 1px solid white;">C22 C26</td><td style="border: 1px solid white;">2</td><td style="border: 1px solid white;">0</td><td style="border: 1px solid white;">None</td><td style="border: 1px solid white;">113781</td><td style="border: 1px solid white;">S</td><td style="border: 1px solid white;">Montreal, PQ / Chesterville, ON</td><td style="border: 1px solid white;">1</td></tr><tr ><td style="font-size:1.02em;background-color:#263133;color:white"><b>2</b></td><td style="border: 1px solid white;">151.55000</td><td style="border: 1px solid white;">female</td><td style="border: 1px solid white;">None</td><td style="border: 1px solid white;">1</td><td style="border: 1px solid white;">25.000</td><td style="border: 1px solid white;">Allison, Mrs. Hudson J C (Bessie Waldo Daniels)</td><td style="border: 1px solid white;">C22 C26</td><td style="border: 1px solid white;">2</td><td style="border: 1px solid white;">0</td><td style="border: 1px solid white;">None</td><td style="border: 1px solid white;">113781</td><td style="border: 1px solid white;">S</td><td style="border: 1px solid white;">Montreal, PQ / Chesterville, ON</td><td style="border: 1px solid white;">1</td></tr><tr ><td style="font-size:1.02em;background-color:#263133;color:white"><b>3</b></td><td style="border: 1px solid white;">0.00000</td><td style="border: 1px solid white;">male</td><td style="border: 1px solid white;">None</td><td style="border: 1px solid white;">1</td><td style="border: 1px solid white;">39.000</td><td style="border: 1px solid white;">Andrews, Mr. Thomas Jr</td><td style="border: 1px solid white;">A36</td><td style="border: 1px solid white;">0</td><td style="border: 1px solid white;">0</td><td style="border: 1px solid white;">None</td><td style="border: 1px solid white;">112050</td><td style="border: 1px solid white;">S</td><td style="border: 1px solid white;">Belfast, NI</td><td style="border: 1px solid white;">0</td></tr><tr ><td style="font-size:1.02em;background-color:#263133;color:white"><b>4</b></td><td style="border: 1px solid white;">49.50420</td><td style="border: 1px solid white;">male</td><td style="border: 1px solid white;">22</td><td style="border: 1px solid white;">1</td><td style="border: 1px solid white;">71.000</td><td style="border: 1px solid white;">Artagaveytia, Mr. Ramon</td><td style="border: 1px solid white;">None</td><td style="border: 1px solid white;">0</td><td style="border: 1px solid white;">0</td><td style="border: 1px solid white;">None</td><td style="border: 1px solid white;">PC 17609</td><td style="border: 1px solid white;">C</td><td style="border: 1px solid white;">Montevideo, Uruguay</td><td style="border: 1px solid white;">0</td></tr><tr><td style="border-top: 1px solid white;background-color:#263133;color:white"></td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td></tr></table>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>&lt;object&gt;  Name: titanic, Number of rows: 1234, Number of columns: 14
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[53]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Turning the SQL on</span>
<span class="n">titanic</span><span class="o">.</span><span class="n">sql_on_off</span><span class="p">()</span>
<span class="c1"># Turning the Time on</span>
<span class="n">titanic</span><span class="o">.</span><span class="n">time_on_off</span><span class="p">()</span>
<span class="c1"># Describing the Dataset</span>
<span class="n">titanic</span><span class="o">.</span><span class="n">describe</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>



<div class="output_html rendered_html output_subarea ">
<h4 style = 'color : #444444; text-decoration : underline;'>Computes the descriptive statistics of all the numerical columns using SUMMARIZE_NUMCOL.</h4>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>



<div class="output_html rendered_html output_subarea ">
 &emsp;  SELECT <br> &emsp;  &emsp;  SUMMARIZE_NUMCOL("fare", "body", "pclass", "age", "parch", "survived", "sibsp") OVER () &emsp; <br> &emsp;  FROM <br> "public"."titanic"
</div>

</div>

<div class="output_area">

<div class="prompt"></div>



<div class="output_html rendered_html output_subarea ">
<div style = 'border : 1px dashed black; width : 100%'></div>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>



<div class="output_html rendered_html output_subarea ">
<div><b>Elapsed Time : </b> 0.019838809967041016</div>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>



<div class="output_html rendered_html output_subarea ">
<div style = 'border : 1px dashed black; width : 100%'></div>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>



<div class="output_html rendered_html output_subarea ">
<h4 style = 'color : #444444; text-decoration : underline;'>Computes the different aggregations.</h4>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>



<div class="output_html rendered_html output_subarea ">
 &emsp;  SELECT <br> &emsp;  &emsp;  COUNT(DISTINCT "age"), <br> &emsp;  &emsp;  COUNT(DISTINCT "body"), <br> &emsp;  &emsp;  COUNT(DISTINCT "fare"), <br> &emsp;  &emsp;  COUNT(DISTINCT "parch"), <br> &emsp;  &emsp;  COUNT(DISTINCT "pclass"), <br> &emsp;  &emsp;  COUNT(DISTINCT "sibsp"), <br> &emsp;  &emsp;  COUNT(DISTINCT "survived") &emsp; <br> &emsp;  FROM <br> "public"."titanic" LIMIT 1
</div>

</div>

<div class="output_area">

<div class="prompt"></div>



<div class="output_html rendered_html output_subarea ">
<div style = 'border : 1px dashed black; width : 100%'></div>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>



<div class="output_html rendered_html output_subarea ">
<div><b>Elapsed Time : </b> 0.06264996528625488</div>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>



<div class="output_html rendered_html output_subarea ">
<div style = 'border : 1px dashed black; width : 100%'></div>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>



<div class="output_html rendered_html output_subarea ">
<table style="border-collapse: collapse; border: 2px solid white"><tr ><td style="font-size:1.02em;background-color:#263133;color:white"><b></b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>count</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>mean</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>std</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>min</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>25%</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>50%</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>75%</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>max</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>unique</b></td></tr><tr ><td style="font-size:1.02em;background-color:#263133;color:white"><b>age</b></td><td style="border: 1px solid white;">997</td><td style="border: 1px solid white;">30.1524573721163</td><td style="border: 1px solid white;">14.4353046299159</td><td style="border: 1px solid white;">0.33</td><td style="border: 1px solid white;">21.0</td><td style="border: 1px solid white;">28.0</td><td style="border: 1px solid white;">39.0</td><td style="border: 1px solid white;">80.0</td><td style="border: 1px solid white;">96.0</td></tr><tr ><td style="font-size:1.02em;background-color:#263133;color:white"><b>body</b></td><td style="border: 1px solid white;">118</td><td style="border: 1px solid white;">164.14406779661</td><td style="border: 1px solid white;">96.5760207557808</td><td style="border: 1px solid white;">1.0</td><td style="border: 1px solid white;">79.25</td><td style="border: 1px solid white;">160.5</td><td style="border: 1px solid white;">257.5</td><td style="border: 1px solid white;">328.0</td><td style="border: 1px solid white;">118.0</td></tr><tr ><td style="font-size:1.02em;background-color:#263133;color:white"><b>fare</b></td><td style="border: 1px solid white;">1233</td><td style="border: 1px solid white;">33.963793673966</td><td style="border: 1px solid white;">52.6460729831293</td><td style="border: 1px solid white;">0.0</td><td style="border: 1px solid white;">7.8958</td><td style="border: 1px solid white;">14.4542</td><td style="border: 1px solid white;">31.3875</td><td style="border: 1px solid white;">512.3292</td><td style="border: 1px solid white;">277.0</td></tr><tr ><td style="font-size:1.02em;background-color:#263133;color:white"><b>parch</b></td><td style="border: 1px solid white;">1234</td><td style="border: 1px solid white;">0.378444084278768</td><td style="border: 1px solid white;">0.868604707790393</td><td style="border: 1px solid white;">0.0</td><td style="border: 1px solid white;">0.0</td><td style="border: 1px solid white;">0.0</td><td style="border: 1px solid white;">0.0</td><td style="border: 1px solid white;">9.0</td><td style="border: 1px solid white;">8.0</td></tr><tr ><td style="font-size:1.02em;background-color:#263133;color:white"><b>pclass</b></td><td style="border: 1px solid white;">1234</td><td style="border: 1px solid white;">2.28444084278768</td><td style="border: 1px solid white;">0.842485636190292</td><td style="border: 1px solid white;">1.0</td><td style="border: 1px solid white;">1.0</td><td style="border: 1px solid white;">3.0</td><td style="border: 1px solid white;">3.0</td><td style="border: 1px solid white;">3.0</td><td style="border: 1px solid white;">3.0</td></tr><tr ><td style="font-size:1.02em;background-color:#263133;color:white"><b>sibsp</b></td><td style="border: 1px solid white;">1234</td><td style="border: 1px solid white;">0.504051863857374</td><td style="border: 1px solid white;">1.04111727241629</td><td style="border: 1px solid white;">0.0</td><td style="border: 1px solid white;">0.0</td><td style="border: 1px solid white;">0.0</td><td style="border: 1px solid white;">1.0</td><td style="border: 1px solid white;">8.0</td><td style="border: 1px solid white;">7.0</td></tr><tr ><td style="font-size:1.02em;background-color:#263133;color:white"><b>survived</b></td><td style="border: 1px solid white;">1234</td><td style="border: 1px solid white;">0.364667747163696</td><td style="border: 1px solid white;">0.481532018641288</td><td style="border: 1px solid white;">0.0</td><td style="border: 1px solid white;">0.0</td><td style="border: 1px solid white;">0.0</td><td style="border: 1px solid white;">1.0</td><td style="border: 1px solid white;">1.0</td><td style="border: 1px solid white;">2.0</td></tr></table>
</div>

</div>

<div class="output_area">

<div class="prompt output_prompt">Out[53]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;object&gt;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="See-Also">See Also<a class="anchor-link" href="#See-Also">&#182;</a></h3><table id="seealso">
    <tr><td><a href="../sql_on_off">vDataFrame.sql_on_off</a></td> <td>Displays each query generated by the vDataFrame.</td></tr>
</table>
</div>
</div>
</div>