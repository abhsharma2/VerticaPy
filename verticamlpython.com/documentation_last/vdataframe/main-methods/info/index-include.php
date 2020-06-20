<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="vDataFrame.info">vDataFrame.info<a class="anchor-link" href="#vDataFrame.info">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">vDataFrame</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Displays information about the different vDataFrame transformations.</p>

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
<div class="prompt input_prompt">In&nbsp;[1]:</div>
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
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Doing some transformations</span>
<span class="n">titanic</span><span class="o">.</span><span class="n">get_dummies</span><span class="p">()</span>
<span class="n">titanic</span><span class="o">.</span><span class="n">normalize</span><span class="p">(</span><span class="n">method</span> <span class="o">=</span> <span class="s2">&quot;minmax&quot;</span><span class="p">)</span>
<span class="c1"># Printing all the transformations</span>
<span class="n">titanic</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>The vDataFrame was modified many times: 
 * {Mon Apr 27 17:53:48 2020} [Get Dummies]: One hot encoder was applied to the vcolumn &#34;sex&#34;
1 feature(s) was/were created: &#34;sex_female&#34;.
 * {Mon Apr 27 17:53:48 2020} [Get Dummies]: One hot encoder was applied to the vcolumn &#34;pclass&#34;
2 feature(s) was/were created: &#34;pclass_1&#34;, &#34;pclass_2&#34;.
 * {Mon Apr 27 17:53:48 2020} [Get Dummies]: One hot encoder was applied to the vcolumn &#34;parch&#34;
7 feature(s) was/were created: &#34;parch_0&#34;, &#34;parch_1&#34;, &#34;parch_2&#34;, &#34;parch_3&#34;, &#34;parch_4&#34;, &#34;parch_5&#34;, &#34;parch_6&#34;.
 * {Mon Apr 27 17:53:48 2020} [Get Dummies]: One hot encoder was applied to the vcolumn &#34;embarked&#34;
2 feature(s) was/were created: &#34;embarked_C&#34;, &#34;embarked_Q&#34;.
 * {Mon Apr 27 17:53:48 2020} [Get Dummies]: One hot encoder was applied to the vcolumn &#34;sibsp&#34;
6 feature(s) was/were created: &#34;sibsp_0&#34;, &#34;sibsp_1&#34;, &#34;sibsp_2&#34;, &#34;sibsp_3&#34;, &#34;sibsp_4&#34;, &#34;sibsp_5&#34;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;fare&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;body&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;pclass&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;age&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;parch&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;survived&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;sibsp&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;sex_female&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;pclass_1&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;pclass_2&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;parch_0&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;parch_1&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;parch_2&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;parch_3&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;parch_4&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;parch_5&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;parch_6&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;embarked_C&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;embarked_Q&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;sibsp_0&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;sibsp_1&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;sibsp_2&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;sibsp_3&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;sibsp_4&#34;&#39; was normalized with the method &#39;minmax&#39;.
 * {Mon Apr 27 17:53:48 2020} [Normalize]: The vcolumn &#39;&#34;sibsp_5&#34;&#39; was normalized with the method &#39;minmax&#39;.
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>



<div class="output_html rendered_html output_subarea ">
<table style="border-collapse: collapse; border: 2px solid white"><tr ><td style="font-size:1.02em;background-color:#263133;color:white"><b></b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>fare</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>sex</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>body</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>pclass</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>age</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>name</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>cabin</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>parch</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>survived</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>boat</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>ticket</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>embarked</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>home.dest</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>sibsp</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>sex_female</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>pclass_1</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>pclass_2</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>parch_0</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>parch_1</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>parch_2</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>parch_3</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>parch_4</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>parch_5</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>parch_6</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>embarked_C</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>embarked_Q</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>sibsp_0</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>sibsp_1</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>sibsp_2</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>sibsp_3</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>sibsp_4</b></td><td style="font-size:1.02em;background-color:#263133;color:white"><b>sibsp_5</b></td></tr><tr ><td style="font-size:1.02em;background-color:#263133;color:white"><b>0</b></td><td style="border: 1px solid white;">0.295805899800363</td><td style="border: 1px solid white;">female</td><td style="border: 1px solid white;">None</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0.020961466047446</td><td style="border: 1px solid white;">Allison, Miss. Helen Loraine</td><td style="border: 1px solid white;">C22 C26</td><td style="border: 1px solid white;">0.222222222222222</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">None</td><td style="border: 1px solid white;">113781</td><td style="border: 1px solid white;">S</td><td style="border: 1px solid white;">Montreal, PQ / Chesterville, ON</td><td style="border: 1px solid white;">0.125000000000000</td><td style="border: 1px solid white;">1.000000000000000</td><td style="border: 1px solid white;">1.000000000000000</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">1.000000000000000</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">1.000000000000000</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td></tr><tr ><td style="font-size:1.02em;background-color:#263133;color:white"><b>1</b></td><td style="border: 1px solid white;">0.295805899800363</td><td style="border: 1px solid white;">male</td><td style="border: 1px solid white;">0.409785932721713</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0.372411196184260</td><td style="border: 1px solid white;">Allison, Mr. Hudson Joshua Creighton</td><td style="border: 1px solid white;">C22 C26</td><td style="border: 1px solid white;">0.222222222222222</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">None</td><td style="border: 1px solid white;">113781</td><td style="border: 1px solid white;">S</td><td style="border: 1px solid white;">Montreal, PQ / Chesterville, ON</td><td style="border: 1px solid white;">0.125000000000000</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">1.000000000000000</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">1.000000000000000</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">1.000000000000000</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td></tr><tr ><td style="font-size:1.02em;background-color:#263133;color:white"><b>2</b></td><td style="border: 1px solid white;">0.295805899800363</td><td style="border: 1px solid white;">female</td><td style="border: 1px solid white;">None</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0.309652315802686</td><td style="border: 1px solid white;">Allison, Mrs. Hudson J C (Bessie Waldo Daniels)</td><td style="border: 1px solid white;">C22 C26</td><td style="border: 1px solid white;">0.222222222222222</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">None</td><td style="border: 1px solid white;">113781</td><td style="border: 1px solid white;">S</td><td style="border: 1px solid white;">Montreal, PQ / Chesterville, ON</td><td style="border: 1px solid white;">0.125000000000000</td><td style="border: 1px solid white;">1.000000000000000</td><td style="border: 1px solid white;">1.000000000000000</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">1.000000000000000</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">1.000000000000000</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td></tr><tr ><td style="font-size:1.02em;background-color:#263133;color:white"><b>3</b></td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">male</td><td style="border: 1px solid white;">None</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0.485377180871093</td><td style="border: 1px solid white;">Andrews, Mr. Thomas Jr</td><td style="border: 1px solid white;">A36</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">None</td><td style="border: 1px solid white;">112050</td><td style="border: 1px solid white;">S</td><td style="border: 1px solid white;">Belfast, NI</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">1.000000000000000</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">1.000000000000000</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">1.000000000000000</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td></tr><tr ><td style="font-size:1.02em;background-color:#263133;color:white"><b>4</b></td><td style="border: 1px solid white;">0.096625763278767</td><td style="border: 1px solid white;">male</td><td style="border: 1px solid white;">0.064220183486239</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0.887034015313167</td><td style="border: 1px solid white;">Artagaveytia, Mr. Ramon</td><td style="border: 1px solid white;">None</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">None</td><td style="border: 1px solid white;">PC 17609</td><td style="border: 1px solid white;">C</td><td style="border: 1px solid white;">Montevideo, Uruguay</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">1.000000000000000</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">1.000000000000000</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">1.000000000000000</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">1.000000000000000</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td><td style="border: 1px solid white;">0E-15</td></tr><tr><td style="border-top: 1px solid white;background-color:#263133;color:white"></td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td><td style="border: 1px solid white;">...</td></tr></table>
</div>

</div>

<div class="output_area">

<div class="prompt output_prompt">Out[2]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;object&gt;  Name: titanic, Number of rows: 1234, Number of columns: 32</pre>
</div>

</div>

</div>
</div>

</div>