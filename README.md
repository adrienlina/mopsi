This is a project of Cyrille Vessaire and Adrien Lina for their MOPSI course at École des Ponts ParisTech. It aims to show the cutoff phenomenon a graphic example.

We have a square grid of _2n_ squares, the _n^2_ squares in the middle are white, while the others are black. We choose a random square, and flip its color. And do it again. According to the mixing theory (based on Markov Chains theory), there should be a cutoff phenomenon at some point. The goal is to have the user stop the flippings when he thinks the distribution of the colored square is uniform. By making several tries, we hope to experimentally find the value of the cutoff.

It is coded with love in Python and uses the Pygame Library.

Reference : [https://media.readthedocs.org/pdf/pygame/latest/pygame.pdf] Pygame Documentation
