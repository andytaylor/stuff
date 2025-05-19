# Quarterly Connection

## Releases

### 7.12.2 Release

Released 7.12.2 with a focus on customer fixes
- Another attempt at time boxing a release, didn't hit the date planned because of outages and build issues but I deem this a success as we managed to release CR1 and held of adding more fixes with an aim to quickly follow up with 7.12.2
- Planned release Schedule and updated product pages

## Product Security

### Threat Model AMQ Broker

Generate and address findings in threat model for AMQ Broker
- All raised Jiras complete and closed. Took quite a lot of the time, The survey is more aimed at Applications rather than Integration Frameworks so a lot of the Jiras raised didn't really make sense. An example of this is Jiras around Authentication and whether or not we used the recommended methods, of course this only really makes sense for an Application.
- Carried out the survey and walked thru with Ted the security issues that need checking. These were all raised as jiras, 39 in all.
- sd elements https://redhat.sdelements.com/bunits/psse-secure-development/group-2-extended-functionality-offerings/amq-broker/
- Broker Threat Model https://issues.redhat.com/browse/ENTMQBR-8344

## Development

### New Artemis Console

Completed All Engineering tasks wrt the new console based on HawtIO
- As of September all development was complete, new repos created at Apache and prodctisation pipelines in place. Next steps to release upstream, test and release as a standalone console.

### QC Creator

Developed An application that creates a quarterly Connection Summary from my Smartsheet Task board

## Planning and Process

### BCP table Top Exercise

Prepared the tabletop discussion with Kirti and delivered the exercise to the subset of the team
- Improvements to the plan were identified and the plan was updated.
- The session seemed to go well, lots of input from the BCP memebers as well as other inviteees
- Spent quite a lot of time preparing the deck with kirti Kareley. Some good collaboration but this was a time consuming process
- Month<TBD> 2024 P&GE_AMQ_WorkforceUnavailable_ScenarioPlan https://docs.google.com/document/d/1W_0e7BTe-kYUr5qDsJAD92b4k81TYgIVT8qBOXEnt2U/edit?usp=drive_web

### 7.12.1 retrospective

Scheduled and Ran a 7.12.1 retrospective with the team
- Personally this is a new string to my bow and something I will carry on with.
- This is something that the team hasn't done since we lost our program manager and went self service. Most of the the team participated and we identified some improvements that we can make which included, tracking team holidays as part of the planning,
- Miro Sailboat Retrospective https://miro.com/app/board/uXjVKwu6CsU=/

### Agile Transformation

Made progress on the "OKR 2 - Accelerating our Agile journey" wrt what processes we can further improve
- Retrospectively story pointed last micro release to start obtaining metrics around velocity
- defined an initial story pointing process that is simple 1,2,3 and is simple to start with
- Worked with the team to define a definition of done and ready
- Definition of Ready/Done https://docs.google.com/document/d/11JtYWbUL3YNXlsEqTYeRfKHxwXZA8Cy1paXClJhbaxw/edit?usp=drive_web

## Employee Benefits

### 2024 Q2 Vic

Worked with Roddie and awarded Bonuses for team

### Promotions for 2024 Q3

Worked with Roddie to prepare promo packages for Howard Gao and Marjina Sarawan
- Approved Howard's promo and submitted in workday for October 1st
- Approved Marjina's promotion and submitted in Workday for October 1st

### Salary Adjustments for Q4

Worked with Roddie to decide who should receive Increases and how much
- This was a very short cycle and I was on PTO so I spent less time reviewing the adjustments than I normally would
- Salary Adjustments completed in Workday. Since we had 2 promotions to allocate this proved pretty tricky. I managed to allocate to everyone who was due an increase but only the target amount.

### Equity for Q3

Worked with Roddie to allocate equity for Associates
- The move to a yearly cycle was also challenging as Deferring meant an associate may have to wait a year. An example of this was Rakhi, recently promoted to SE and holds no equity I would like to change that but I felt this as a lower priority then increasing the equity of some more experienced Associates.
- This was a short cycle and I was on PTO so It was challenging
- Equity Submitted in Workday

## People Management

### Quarterly Connection Q2

Completed all QC's in workday
- As always Quarterly Connection input from associates is mixed, either very little or a lot. I have found that the newer associates embrace the process more. I have to think about how I can improve the other associates to  improve

### Talent Review Q2 24

completed talent reviews and calibrations with Roddie

## Presentations

### AMQ Overview AEI All hands

prepared and presented AMQ Overview with Roddie
- The presentation seemed to go down well and we had some positive feedback. Roddie and I even received callouts via the Red Hat reward zone from our own associates.
- 2024.06.27 AEI All-Hands - AMQ https://docs.google.com/presentation/d/1i5mmNH1AUcxEjpX4WTU_0zjGttQ0jF1K06SpxluI9Wg/edit?usp=drive_web
- 2024.07.11 AEI All-Hands - AMQ https://docs.google.com/presentation/d/1LJDpwS9KrvlNftgiSx7JjylhxRO3QMUB1YA-13ZQmmI/edit?usp=drive_web

### Provide Enablement Training for AMQ 7.12.0

Support team need training on the new features of AMQ 7.12.0, arrange 2 sessions and ask engineers to provide material
- 2 Sessions were given that covered in detail most of the enhancements delivered. The whole team contributed and we received positive feedback from the audience. This also led to further collaboration afterwards
- 7.12.0 Enablement Training Topics https://docs.google.com/document/d/1pQNHgl1wH-cRP0wroxtN-2N3a0b_yQ7PUOZcvSgKLc0/edit?usp=drive_web

## Customer Engagement

### Barclays Engagement

Working to get Barclays Migrated from 6 to 7
- Escalation raised in July. Barclays have had to delay their go live for lots of issues around using mirroring ad Replication at the same time. This was not a usecase that was envisaged and hence is very buggy. Ive been working with the engineering and broader team to help get them on track.

### Fedex Engagement

working to improve automation and discuss message compression
- We have been working closely with the Ansible team to help deliver the automation they ask for, Andrew Block is working directly with Fedex and their testing begins next week (October 1st). Engineering is supporting Andrew. This automation is driving fedex to sign a new multi million dollar deal sometime Q4
- Several meetings and offline discussions around introducing message compression to the Qpid Client and Broker. We explained to the customer the challenges of adding to the product around spec compliance and other caveats and the customer has agreed to try a POC in their own Client Wrapper

### UPS Engagement

Delivered the new console to UPS via a patched release

