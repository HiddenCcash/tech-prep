# What is Upoop?

Upoop is a software-as-a-service that allows customers to upload DNA samples of a dog as well as submit stool samples for DNA-matching identification.

According to a The Seattle Times [article](https://www.seattletimes.com/seattle-news/eastside/6000-pounds-of-dog-poop-a-day-kirkland-locked-in-dirty-war/) 20,000 dogs can produce 6,000 pounds of waste a day. Many dog owners, for various reasons, do not pick up after their pet which leaves residenetial areas, parks, and sidewalks littered with fecal matter capable of spreading disease and polluting water. Upoop's seeks to incentivize dog owners to pick up after their pets by allowing property owners to submit fecal samples for dog/owner identification.

# Requirements

Functional
Users will be able to upload text information about the owner and dog
Users will be able to query the system to check for a dog-match - by submitting a dog-owner identification

Not In Scope
Creating a dog-owner ID/signature based on a stool sample. It is simplified so that a user sees a stool sample and automagically converts that to a dog-owner signature (Ie, no DNA synsthesizing)

# Design Considerations

# Estimations

Costs, Usage, Limits, etc.

The service will be write with an approximate read-to-write ratio of 20:1.
In this case, a read will be a identification check based on the user providing a unique stool signature.
The estimated number of dogs in the US is slightly under 100 million and the estimated number of stool checks to be processed per day will be 100,000.
As such, the estimated number of new dog-owner data writes will be 10,000 per day.

# Notes

The template used for generating this system design is taken from the Educative.io's online tutorial [Grokking the System Design Interview](https://www.educative.io/courses/grokking-the-system-design-interview/3jyvQ3pg6KO)
