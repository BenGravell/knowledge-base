<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Tire-Force Ellipse (Friction Ellipse) and Tire Characteristics

Topics include Vehicle dynamics, Tire modeling, Friction ellipse, Road vehicle control, Braking, Cornering, Traction limits.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Explains the tire-force ellipse as an engineering model for the tradeoff between longitudinal and lateral tire forces. The paper is a compact vehicle-dynamics reference: it connects friction limits, braking/cornering behavior, and tire-characteristic curves in a form useful for safety analysis and control design.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The tire-force ellipse and tire-force circle (more frequently referred to as the friction ellipse and the friction circle, respectively) have been used for many years to qualitatively illustrate the concept of tire-road force interaction, particularly the force-limiting behavior for combined braking and steering (combined tire forces). Equations of the tire-force circle/ellipse, or, more specifically, the force limit envelope, in its idealized form have also been used in the development of quantitative models of combined tire forces used in vehicle dynamic simulation software. Comparisons of this idealized tire-force circle/ellipse using a simple bilinear tire force model and using actual tire data show that it provides only a limited, simplified notion of combined tire forces due to its lack of dependence upon the slip angle and traction slip. Furthermore, these comparisons show that the idealized tire-force circle/ellipse does not represent actual tire behavior, even approximately, since it is incapable of modeling the nonlinear behavior of tires. For this reason, the idealized tire-force circle/ellipse should not be used as a quantitative tire-force model particularly because superior validated models of nonlinear behavior of tires exist and are widely available.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Here a development is presented of a more realistic version of the tire-force circle/ellipse which incorporates slip angle, traction slip and the actual nonlinear tire-force. Because of the complexity of nonlinear tire force behavior the Fy - Fx force relationship is not a true ellipse and the force limit is dependent on the kinematic slip angle and traction slip variables, a and s, respectively.
