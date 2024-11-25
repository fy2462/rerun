// DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/rust/api.rs
// Based on "crates/store/re_types/definitions/rerun/testing/components/fuzzy.fbs".

#![allow(unused_imports)]
#![allow(unused_parens)]
#![allow(clippy::clone_on_copy)]
#![allow(clippy::cloned_instead_of_copied)]
#![allow(clippy::map_flatten)]
#![allow(clippy::needless_question_mark)]
#![allow(clippy::new_without_default)]
#![allow(clippy::redundant_closure)]
#![allow(clippy::too_many_arguments)]
#![allow(clippy::too_many_lines)]

use ::re_types_core::external::arrow2;
use ::re_types_core::ComponentName;
use ::re_types_core::SerializationResult;
use ::re_types_core::{ComponentBatch, MaybeOwnedComponentBatch};
use ::re_types_core::{DeserializationError, DeserializationResult};

#[derive(Clone, Debug, Default, PartialEq)]
pub struct AffixFuzzer11(pub Option<::re_types_core::ArrowBuffer<f32>>);

impl ::re_types_core::SizeBytes for AffixFuzzer11 {
    #[inline]
    fn heap_size_bytes(&self) -> u64 {
        self.0.heap_size_bytes()
    }

    #[inline]
    fn is_pod() -> bool {
        <Option<::re_types_core::ArrowBuffer<f32>>>::is_pod()
    }
}

impl From<Option<::re_types_core::ArrowBuffer<f32>>> for AffixFuzzer11 {
    #[inline]
    fn from(many_floats_optional: Option<::re_types_core::ArrowBuffer<f32>>) -> Self {
        Self(many_floats_optional)
    }
}

impl From<AffixFuzzer11> for Option<::re_types_core::ArrowBuffer<f32>> {
    #[inline]
    fn from(value: AffixFuzzer11) -> Self {
        value.0
    }
}

impl std::ops::Deref for AffixFuzzer11 {
    type Target = Option<::re_types_core::ArrowBuffer<f32>>;

    #[inline]
    fn deref(&self) -> &Option<::re_types_core::ArrowBuffer<f32>> {
        &self.0
    }
}

impl std::ops::DerefMut for AffixFuzzer11 {
    #[inline]
    fn deref_mut(&mut self) -> &mut Option<::re_types_core::ArrowBuffer<f32>> {
        &mut self.0
    }
}

::re_types_core::macros::impl_into_cow!(AffixFuzzer11);

impl ::re_types_core::Loggable for AffixFuzzer11 {
    #[inline]
    fn arrow_datatype() -> arrow::datatypes::DataType {
        #![allow(clippy::wildcard_imports)]
        use arrow::datatypes::*;
        DataType::List(std::sync::Arc::new(Field::new(
            "item",
            DataType::Float32,
            false,
        )))
    }

    fn to_arrow_opt<'a>(
        data: impl IntoIterator<Item = Option<impl Into<::std::borrow::Cow<'a, Self>>>>,
    ) -> SerializationResult<arrow::array::ArrayRef>
    where
        Self: Clone + 'a,
    {
        #![allow(clippy::wildcard_imports)]
        #![allow(clippy::manual_is_variant_and)]
        use ::re_types_core::{Loggable as _, ResultExt as _};
        use arrow::{array::*, buffer::*, datatypes::*};

        #[allow(unused)]
        fn as_array_ref<T: Array + 'static>(t: T) -> ArrayRef {
            std::sync::Arc::new(t) as ArrayRef
        }
        Ok({
            let (somes, data0): (Vec<_>, Vec<_>) = data
                .into_iter()
                .map(|datum| {
                    let datum: Option<::std::borrow::Cow<'a, Self>> = datum.map(Into::into);
                    let datum = datum.map(|datum| datum.into_owned().0).flatten();
                    (datum.is_some(), datum)
                })
                .unzip();
            let data0_validity: Option<arrow::buffer::NullBuffer> = {
                let any_nones = somes.iter().any(|some| !*some);
                any_nones.then(|| somes.into())
            };
            {
                let offsets = arrow::buffer::OffsetBuffer::<i32>::from_lengths(
                    data0
                        .iter()
                        .map(|opt| opt.as_ref().map_or(0, |datum| datum.num_instances())),
                );
                let data0_inner_data: ScalarBuffer<_> = data0
                    .iter()
                    .flatten()
                    .map(|b| b.as_slice())
                    .collect::<Vec<_>>()
                    .concat()
                    .into();
                let data0_inner_validity: Option<arrow::buffer::NullBuffer> = None;
                as_array_ref(ListArray::try_new(
                    std::sync::Arc::new(Field::new("item", DataType::Float32, false)),
                    offsets,
                    as_array_ref(PrimitiveArray::<Float32Type>::new(
                        data0_inner_data,
                        data0_inner_validity,
                    )),
                    data0_validity,
                )?)
            }
        })
    }

    fn from_arrow2_opt(
        arrow_data: &dyn arrow2::array::Array,
    ) -> DeserializationResult<Vec<Option<Self>>>
    where
        Self: Sized,
    {
        #![allow(clippy::wildcard_imports)]
        use ::re_types_core::{Loggable as _, ResultExt as _};
        use arrow::datatypes::*;
        use arrow2::{array::*, buffer::*};
        Ok({
            let arrow_data = arrow_data
                .as_any()
                .downcast_ref::<arrow2::array::ListArray<i32>>()
                .ok_or_else(|| {
                    let expected = Self::arrow_datatype();
                    let actual = arrow_data.data_type().clone();
                    DeserializationError::datatype_mismatch(expected, actual)
                })
                .with_context("rerun.testing.components.AffixFuzzer11#many_floats_optional")?;
            if arrow_data.is_empty() {
                Vec::new()
            } else {
                let arrow_data_inner = {
                    let arrow_data_inner = &**arrow_data.values();
                    arrow_data_inner
                        .as_any()
                        .downcast_ref::<Float32Array>()
                        .ok_or_else(|| {
                            let expected = DataType::Float32;
                            let actual = arrow_data_inner.data_type().clone();
                            DeserializationError::datatype_mismatch(expected, actual)
                        })
                        .with_context(
                            "rerun.testing.components.AffixFuzzer11#many_floats_optional",
                        )?
                        .values()
                };
                let offsets = arrow_data.offsets();
                arrow2::bitmap::utils::ZipValidity::new_with_validity(
                    offsets.iter().zip(offsets.lengths()),
                    arrow_data.validity(),
                )
                .map(|elem| {
                    elem.map(|(start, len)| {
                        let start = *start as usize;
                        let end = start + len;
                        if end > arrow_data_inner.len() {
                            return Err(DeserializationError::offset_slice_oob(
                                (start, end),
                                arrow_data_inner.len(),
                            ));
                        }

                        #[allow(unsafe_code, clippy::undocumented_unsafe_blocks)]
                        let data = unsafe {
                            arrow_data_inner
                                .clone()
                                .sliced_unchecked(start, end - start)
                        };
                        let data = ::re_types_core::ArrowBuffer::from(data);
                        Ok(data)
                    })
                    .transpose()
                })
                .collect::<DeserializationResult<Vec<Option<_>>>>()?
            }
            .into_iter()
        }
        .map(Ok)
        .map(|res| res.map(|v| Some(Self(v))))
        .collect::<DeserializationResult<Vec<Option<_>>>>()
        .with_context("rerun.testing.components.AffixFuzzer11#many_floats_optional")
        .with_context("rerun.testing.components.AffixFuzzer11")?)
    }
}

impl ::re_types_core::Component for AffixFuzzer11 {
    #[inline]
    fn name() -> ComponentName {
        "rerun.testing.components.AffixFuzzer11".into()
    }
}
