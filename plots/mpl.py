# Help: python3 matplotlib.py --help
import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def main():
  parser = argparse.ArgumentParser(
    description='',
    epilog='Author: Marcel Saaro'
  )
  parser.add_argument(
    "-i", "--input-file",
    type=str,
    required=True,
    help='The input file must be a csv.',
  )
  parser.add_argument(
    "-c", "--column-to-plot",
    type=str,
    required=True,
    help='The column in the csv.',
  )
  parser.add_argument(
    "-p", "--plot-file",
    type=str,
    required=True,
    help='Path of the plot file. None existing folders in the path will be created.',
  )
  args = parser.parse_args()

  input_file = Path(args.input_file)
  column = args.column_to_plot
  plot_file = Path(args.plot_file)

  # -------------------------------------------------------------------------
  # Load the data
  # -------------------------------------------------------------------------
  df = pd.read_csv(input_file)


  # -------------------------------------------------------------------------
  # Plot
  # -------------------------------------------------------------------------
  fig = plt.figure(
    figsize=(6.4, 4.8), # in inch
    # facecolor='white',
  )
  # fig.suptitle(
  #   'Title',
  #   x=0.5, y=0.98,
  #   fontsize=14
  # )

  gs = fig.add_gridspec(
    nrows=1, ncols=1,
    left=0.125, right=0.9,
    bottom=0.11, top=0.88,
    hspace=0.2, wspace=0.2,
  )

  # Strain Rate Profile
  ax = fig.add_subplot(
    gs[0, 0],
    # aspect='equal',
    # facecolor='white',
    title='Title',
    xlabel='x-axis with latex $a^2$',
    # xlim=(np.min(x), np.max(x)),
    # xticks=[], # Hide if empty
    # xticklabels=[], # Hide if empty
    ylabel='y-axis',
    # ylim=(np.min(y), np.max(y)),
    # yticks=[], # Hide if empty
    # yticklabels=[], # Hide if empty
  )
  df[column].plot(ax=ax)

  # Save the figure
  plot_file.parent.mkdir(parents=True, exist_ok=True)
  plt.savefig(plot_file)



if __name__ == "__main__":
  main()
