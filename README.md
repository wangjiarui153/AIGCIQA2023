# AIGCIQA2023
In order to get a better understanding of human visual preferences for AI-generated images based on text prompts, we construct a novel IQA database for AIGIs, termed AIGCIQA2023, which is a collection of generated images derived from six state-of-the-art deep generative models based on 100 text prompts, and corresponding subjective quality ratings from three different perspectives.

We adopt six latest text-to-image generative models, including **Glide, Lafite, DALLE, Stable-diffusion, Unidiffuser, Controlnet** to produce AIGIs.
To ensure content diversity and catch up with the practical application requirements, we collect diverse texts from the [PartiPrompts website](https://github.com/google-research/parti) as the prompts for AIGI generation.
The text prompts can be simple, allowing generative models to produce imaginative results.
They can also be complex, which raises the challenge for generative models.
We select 10 scene categories from the prompt set, and each scene contains 10 challenge categories.
Overall, we collect 100 text prompts (10 scene categories $\times$ 10 challenge categories) from PartiPrompts.
It can be observed that the dataset exhibits a high level of scene diversity, with images generated covering a broad range of challenges.
Then we perform the text-to-image generation based on these models and prompts. Specifically, for each prompt, we generate 4 various images randomly for each generative model. Therefore, the constructed AIGCIQA2023 database totally contains 2400 AIGIs (4 images $\times$ 6 models $\times$ 100 prompts) corresponding to 100 prompts.


![samples_imgs_00](https://github.com/wangjiarui153/AIGCIQA2023/assets/104545370/ab434e91-a766-4de4-babd-1d8fe5cb70c0)


Contact: If you want to get the database please send email to wangjiarui@sjtu.edu.cn
