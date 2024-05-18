# Essy

> ⚠️ 🚧 This project is still pre-v1 and not meant to be easily installable yet.

Easy Static Site Hoster (ESSH, spoken "Essy")

A personal site hosting platform, where you'd need nothing more than a web server, a browser,
and some HTML coding skills, to create your own personal website.

Essy works with a reverse proxy, pointing it at the files and folders that you uploaded, and manages the rest for you :3

## Roadmap

### v1

The first major release, meant to focus on the core functionality of editing static websites.

- [ ] 0.1: [MVP](https://github.com/ShadowJonathan/Essy/milestone/1)
    - Basic utility, such as defining domains, and uploading files
- [ ] 1.0: ["Usable"](https://github.com/ShadowJonathan/Essy/milestone/2)
    - Fool-hardening by checking common problems such as DNS and nginx configuration
    - Automatic TLS certificate management
    - A browser code editor
    - Easy installation
    - Security hardening via an isolated component (as nginx reloads require root permission)
- [ ] 1.1: [Live Editing Preview](https://github.com/ShadowJonathan/Essy/milestone/3)
    - Have the browser code editor support live previews, before committing/saving to the site proper
- [ ] 1.2: [Multi-user](https://github.com/ShadowJonathan/Essy/milestone/6)
    - Allowing multiple users to login to the same instance
    - A split between administrators and users
    - Sharing of domain ownership between users

### v2

A second major release adding more extendability, completely optional.

- [ ] 2.0: [Extensions](https://github.com/ShadowJonathan/Essy/milestone/4)
    - Support static site generators as optional extensions, able to be installed/toggled per domain
    - Code editor will point to setup files of the extension
- [ ] 2.1: [Tweaks](https://github.com/ShadowJonathan/Essy/milestone/5)
    - Allow "tweaking" the output of static site generators
    - These "tweaks" are stored as (HTML) diffs, which are then re-applied on every output
    - All-or-nothing: Tweaks apply, or output is not applied to the site (Disable/fix the tweak to let it pass)

## Anti-commitments

At the moment, we are not focusing on features like the following;

- Enterprise Support
  - Essy is meant to be for personal use, while businesses and such could technically use it,
    we will not focus on supporting features relevant to it (SSO, group management, etc.)

## Maintenance Brief

From Jo (@ShadowJonathan):

> While I want to create Essy, I don't want to be a long-term intensive maintainer of it.
> Maintenance (after v1 or v2) should be low-energy for me, hands-off,
> so I can allocate energy elsewhere for other projects.
>
> I'll put my energy into creating v1 and possibly also v2, but after that, there'll have to be a shift in
> expectations; either I'll be more absent and development will be slower, or someone else will do maintenance for me,
> or this'll be maintained/owned by some other group.
>
> I don't intend to make money off of this, neither do I intend for this to be ever a money-generating revenue;
> the entire point is play and experimentation. So don't expect me to sell it, or whatever that would mean for an
> Open Source Project.

