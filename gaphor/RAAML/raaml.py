# This file is generated by profile_coder.py. DO NOT EDIT!

from __future__ import annotations

from gaphor.core.modeling.properties import (
    association,
    attribute,
    relation_many,
    relation_one,
)
from gaphor.SysML.sysml import Block, DirectedRelationshipPropertyPath
from gaphor.UML import Class, DataType, Dependency, Element, Property, State


class AND(Class):
    pass


class GateDef:
    pass


class AND_Def(GateDef):
    pass


class Situation(Block, Class):
    pass


class AnySituation(Situation):
    pass


class AbstractEvent(AnySituation):
    pass


class AbstractCause(AbstractEvent):
    pass


class DysfunctionalEvent(AbstractEvent):
    pass


class AbstractEffect(DysfunctionalEvent):
    pass


class AbstractFailureMode(DysfunctionalEvent):
    pass


class OperationalCondition(Situation):
    pass


class AbstractOperationalSituation(OperationalCondition):
    pass


class Scenario(AnySituation):
    scenarioStep: relation_many[AnySituation]


class AbstractRisk(Scenario):
    harm: relation_many[AbstractEffect]
    harmPotential: relation_many[HarmPotential]
    trigger: relation_many[AbstractEvent]


class Actuator(Property):
    pass


class BasicEvent(Class):
    pass


class FTAElement(DysfunctionalEvent):
    pass


class EventDef(FTAElement):
    pass


class BasicEventDef(EventDef):
    pass


class Cause(AbstractCause):
    pass


class ConditionalEvent(Class):
    pass


class ConditionalEventDef(EventDef):
    pass


class Signal:
    pass


class ControlAction(Class, DataType, Signal):
    pass


class ControlStructure(Block, Class):
    pass


class ControlledProcess(Property):
    pass


class Controller(Property):
    pass


class ControllingMeasure(Dependency, DirectedRelationshipPropertyPath):
    affects: relation_many[Property]


class Detection(ControllingMeasure, Dependency):
    pass


class DormantEvent(Class):
    pass


class DormantEventDef(EventDef):
    pass


class UnsafeControlAction_Def(Situation):
    Context: relation_one[AbstractOperationalSituation]
    harmPotential: relation_many[HarmPotential]


class Early(UnsafeControlAction_Def):
    pass


class Effect(AbstractEffect):
    pass


class FTATree(FTAElement, Scenario):
    topEvent: relation_one[EventDef]


class Factor(AbstractCause):
    pass


class FailureMode:
    pass


class FailureState(State):
    pass


class Feedback(Class, DataType, Signal):
    pass


class Gate(Class):
    pass


class HarmPotential(AnySituation):
    pass


class Hazard(HarmPotential):
    pass


class HouseEvent(Class):
    pass


class HouseEventDef(EventDef):
    pass


class INHIBIT(Class):
    pass


class INHIBIT_Def(GateDef):
    condition: relation_many[EventDef]


class ProcessModel:
    pass


class InadequateControlExecution(ProcessModel):
    pass


class InadequateControllerDecisions(ProcessModel):
    pass


class InadequateFeedbackAndInputs(ProcessModel):
    pass


class InadequateProcessBehavior(ProcessModel):
    pass


class IntermediateEvent(Class):
    pass


class IntermediateEventDef(EventDef):
    pass


class Late(UnsafeControlAction_Def):
    pass


class Loss(AbstractEffect):
    pass


class LossScenario(Scenario):
    Factor: relation_many[Factor]
    processModel: relation_many[ProcessModel]
    unsafeControlAction: relation_many[UnsafeControlAction_Def]


class MAJORITY_VOTE(Class):
    pass


class MAJORITY_VOTE_Def(GateDef):
    pass


class Mitigation(ControllingMeasure, Dependency):
    pass


class NOT(Class):
    pass


class NOT_Def(GateDef):
    pass


class NotProvided(UnsafeControlAction_Def):
    pass


class OR(Class):
    pass


class OR_Def(GateDef):
    pass


class OperationalSituation(Class):
    pass


class OutOfSequence(UnsafeControlAction_Def):
    pass


class Prevention(ControllingMeasure, Dependency):
    pass


class Provided(UnsafeControlAction_Def):
    pass


class Recommendation(ControllingMeasure, Dependency):
    pass


class RelevantTo(Dependency, DirectedRelationshipPropertyPath):
    pass


class RiskRealization(AbstractRisk):
    pass


class SEQ(Class):
    pass


class SEQ_Def(GateDef):
    pass


class Sensor(Property):
    pass


class Threat(Factor):
    pass


class TopEvent(Class):
    pass


class TopEventDef(EventDef):
    pass


class TransferIn(Property):
    pass


class TransferOut(Class):
    pass


class Tree(Class):
    pass


class UndesiredState(DysfunctionalEvent):
    pass


class Undeveloped(Element):
    pass


class UndevelopedEventDef(EventDef):
    pass


class UnsafeControlAction(Class, FailureMode):
    pass


class Violates(Dependency):
    pass


class XOR(Class):
    pass


class XOR_Def(GateDef):
    pass


class ZeroEvent(Class):
    pass


class ZeroEventDef(EventDef):
    pass


AbstractRisk.harm = association("harm", AbstractEffect, composite=True)
AbstractRisk.harmPotential = association("harmPotential", HarmPotential, composite=True)
AbstractRisk.trigger = association("trigger", AbstractEvent, composite=True)
Block.isEncapsulated = attribute("isEncapsulated", int)
ControllingMeasure.affects = association("affects", Property)
FTATree.topEvent = association("topEvent", EventDef, upper=1, composite=True)
INHIBIT_Def.condition = association("condition", EventDef)
LossScenario.Factor = association("Factor", Factor, composite=True)
LossScenario.processModel = association("processModel", ProcessModel, composite=True)
LossScenario.unsafeControlAction = association(
    "unsafeControlAction", UnsafeControlAction_Def
)
Scenario.scenarioStep = association("scenarioStep", AnySituation, composite=True)
UnsafeControlAction_Def.Context = association(
    "Context", AbstractOperationalSituation, upper=1
)
UnsafeControlAction_Def.harmPotential = association("harmPotential", HarmPotential)
