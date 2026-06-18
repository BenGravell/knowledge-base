Incremental A*

Topics include Incremental search, Lifelong planning A*, A* search, Path planning, Route planning, Dynamic graphs, Heuristic search.

Introduces Lifelong Planning A*, an incremental version of A* that reuses unchanged portions of a previous search tree across related planning problems. The method laid groundwork for later replanning algorithms such as D* Lite by showing how optimal heuristic search can be efficiently updated after graph-cost changes.

Incremental search techniques ﬁnd optimal solutions to series of similar search tasks much faster than is possible by solving each search task from scratch. While researchers have developed incremental versions of uninformed search methods, we develop an incremental version of A*. The ﬁrst search of Lifelong Planning A* is the same as that of A* but all subsequent searches are much faster because it reuses those parts of the previous search tree that are identical to the new search tree. We then present experimental results that demonstrate the advantages of Lifelong Planning A* for simple route planning tasks.
