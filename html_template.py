main_body = """

<html>
    <head>
        <title>Stock picks for Swing</title>
    </head>
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <body>
	<div class="container">
			<table class="table table-striped table-bordered">
				<thead class="thead-dark">
					<tr>
						<th scope="col">Quote</th>
						<th scope="col">Last Price</th>
						<th scope="col">Trend (Compared to first day of previous month)</th>
						<th scope="col">Bullish Probability</th>
					</tr>
				<thead>
				{0}
			</table>
		</div>
    </body>
</html>

"""

table_row = """
<tr>
	<td>{0}</td>
	<td>{1}</td>
	<td><font color="{2}">{3}</font></td>
	<td><font color="{4}">{5}</font></td>
</tr>
"""
