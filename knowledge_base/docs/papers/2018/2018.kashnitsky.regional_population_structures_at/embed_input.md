<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Regional Population Structures at a Glance

Topics include Demography, Population age structure, Population ageing, Ternary colour coding, Compositional data, Choropleth maps, Data visualization, European regions.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Maps the age structures of European regions with ternary colour coding, assigning each region a colour that encodes its relative shares of children, working-age people, and older people. The visualization exposes geographic patterns in population ageing and demographic history at a glance.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Population ageing is a major demographic challenge for humanity. Since population structures evolve slowly and predictably, the demographic, economic, environmental, and social problems of ageing have been anticipated and discussed for many decades. Yet the focus of these discussions has always been the elderly population, with elderly people often defined as those older than a threshold - eg, 65 years or age at retirement - or with a certain number of estimated remaining years of life. Such a focus is quite reasonable and understandable but not entirely correct. Ageing is not exclusively about the size of the elderly population or its proportion of a population; ageing is a function of the entire age distribution of a population. Therefore, to better understand ageing, we need to focus on the evolution of the age structure of the entire population, not just the elderly part. We offer a new approach to investigate the diversity of population ageing in Europe. To map the whole population age structures rather than any single summary measure of ageing, we used ternary colour coding - a technique that maximises the amount of information conveyed by colours. With this approach, each element of a three-dimensional array of compositional data is represented with a unique colour.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The use of colour mixtures to encode multiple data dimensions in a single attribute has been proposed by various authors. To our knowledge, ternary colour coding was first used in the context of map design by Judy Olson. The approach has since been used to map election results in a three-party system, labour force composition by sector, soil textures, composition of arctic sea-ice coverage, and cause-of-death compositions. We used colour coding to explore the differences in population structures across Europe and provide the tools that we developed to streamline its use with R version 3.4.3. The diverse picture of the colour-coded age structure of European regions (figure) indicates the varying stages of population ageing across Europe. The process of population ageing is not occurring uniformly in all areas of Europe and regions differ substantially: eastern Europe is still undergoing demographic dividend, southern European regions are forming a cluster of lowest-low fertility, the baby boomers are ageing in western Europe, urban regions are attracting young professionals and forcing out young parents, and peripheral rural regions are losing their youths forever. Colour coding allows mapping of all regional population structures in Europe simultaneously.

<!-- chunk {"id": "abstract-0005", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This map is not meant to easily inform the reader of the exact population structure in a specific region, rather, it provides a highly detailed snapshot of all the regional population structures, facilitating comparisons between them. One limitation of the approach is that the maps are not easily interpreted and usable by those who are colour blind; however, our generalised function that mixes colours makes it easy to change colours by rotating the colourspace, thus enabling those who are colour blind to use this setting more readily.
