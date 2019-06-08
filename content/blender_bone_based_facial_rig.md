Title: Blender Bone Based Facial Rigging - Part One
Date: 2019-05-29

Before we get started. Don't take this as a definitive way to go about Facial rigging. This is my personal workflow and there probably are a lot of stuff to be improved.

If you want to follow along, you should probably get my add-on [action man](https://github.com/Muream/actionman) that I made to manage action and action constraints easily.

Now let's get to it.

# Overview

The workflow is relatively simple I'm taking full advantages of blender's actions and action constraints.

If you're not a Blender guy a few things to know:

- Blender's bones are just data contained in an `Armature` object.
- An action is where Blender stores animation curves for everything related to a specific object.
  An action cannot (I think?) hold data for multiple object
  Since bones are contained inside one armature object, One action can store the animation data of _all_ the bones of said Armature.
- You can use [Action Constraints](https://docs.blender.org/manual/en/latest/rigging/constraints/relationship/action.html) to drive an object (or bone) with an action. Basically linking that action with an controller's transform channels instead of the timeline.
  If you're from Maya, this is very similar to driven keys. with a few differences:
  - This doesn't lock the constrained object's transform.
  - You can have multiple Action Constraints stacked on top of each other they will add up to each other.
- Bones can be parented _and_ connected to each other.
  * A parented bone is just what you expect the child bone follows the parent.
  * A connected bone will always be attached to its parent's tail. meaning it won't move but can still be rotated/scaled. There's a bunch of things that connected bones allow but I won't get into that here.

So here's how everything is set up on my rig:

- A lot of bones scattered on the face
- One action per pose
- One action constraint per bone contained in each action

# Bone Placement

This is pretty basic stuff. Like I said, this is mostly a bunch of bones scattered on the face.

There are two things that I handle a bit differently:

- Each eyelid bones are actually two bones:
  - The first bone has its head (base) at the center of the eyeball and its tail (tip) placed on the eyelid.
    This lets you rotate this bone easily to close/open the eyelids
  - The second bone is parented to the first one (just parented, not connected) an placed at the tail of the first bone.
- Lip bones are set up similarly:
  - One bone _inside_ the lips. This bone can be used to rotate the lips inside and out
  - A second bone parented to the first one placed where the upper and lower lips are in contact.